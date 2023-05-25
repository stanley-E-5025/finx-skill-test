# FinX Skill Test

This project involves setting up a Django application with multiple SQLite databases. We'll create an abstract base class (ABC) called `DataSource` with a `query` method for filtering and a `name` property.

We'll then implement a concrete class, `DataSourceDjango`, based on this ABC. This class will filter the Django user model in a specified database.

The goal is to perform parallel queries on all databases defined in the settings. The method for achieving this could be async, multiprocessing, threading, or celery, and should be justified in comments.

Finally, we'll combine the results from all data sources into a single data structure, with the data source name as the key.

Here's an example of the final data structure:

```json
{
  "primary": [
    {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@gmail.com"
    }
  ],
  "secondary": [
    {
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@gmail.com"
    }
  ]
}
```

This structure allows for efficient, parallel querying across multiple databases, which is beneficial when dealing with large numbers of data sources.

> Justification why I used Threading for this solution.

- **Asyncio (async/await):** While great for I/O-bound tasks, Django's ORM does not currently support async operations, making asyncio a complicated choice that might not provide any performance benefit.
- **Multiprocessing:** This module is best suited for CPU-bound tasks. However, database querying is typically I/O-bound, so multiprocessing may not provide a significant benefit and has a higher overhead than threading.
- **Threading:** Threading is a good fit for I/O-bound tasks, including database querying. It's lightweight, relatively easy to use, and the GIL (Global Interpreter Lock) in Python isn't an issue here because the time waiting for the database to respond isn't CPU-bound.
- **Celery:** Although a powerful tool for handling asynchronous tasks in a distributed manner, Celery is more complex to set up and use than the other options and may be overkill for this scenario.

Finally, we'll combine the results from all data sources into a single data structure, with the data source name as the key.
