import logging
from abc import ABC, abstractmethod
from .models import Users
from django.db import connections
from django.db.models import Q
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DataSource(ABC):
    @abstractmethod
    def query(self, **kwargs):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class DataSourceDjango(DataSource):
    def __init__(self, name):
        self._name = name

    def query(self, **kwargs):
        return list(
            Users.objects.using(self._name)
            .filter(
                Q(first_name__icontains=kwargs["search"])
                | Q(last_name__icontains=kwargs["search"])
            )
            .values()
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def find_user(search_term):
    def query_db(name):
        ds = DataSourceDjango(name)
        return ds.query(search=search_term)

    results = {}
    with ThreadPoolExecutor() as executor:
        future_to_db = {
            executor.submit(query_db, name): name for name in connections.databases
        }
        for future in as_completed(future_to_db):
            db_name = future_to_db[future]
            try:
                data = future.result()
            except Exception as exc:
                logger.debug(f"{db_name} generated an exception: {exc}")
            else:
                results[db_name] = data
    return results
