from django.core.management.base import BaseCommand
from multi_db_query.models import Users
from faker import Faker

class Command(BaseCommand):
    help = 'Creates random users'

    def handle(self, *args, **options):
        fake = Faker()

        # Iterate over the databases
        for db in ['default', 'secondary']:
            if not Users.objects.using(db).exists():
                for _ in range(200):
                    Users.objects.using(db).create(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        email=fake.email(),
                    )
