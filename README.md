# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

The actual app is under `app/` with its `app/settings.py`, `app/app.py`
and its configuration in `app/secrets/config.json`.
The build is in `app/Dockerfile`.

For testing there is a `testing_app.py`, the actual tests
and testdata are under `test/`.
Start the app and testing app via `docker-compose.yml`
and run tests with `docker-compose run tests pytest test`.

# TODO

- properly separate the app from the tests
- deploy startegy
