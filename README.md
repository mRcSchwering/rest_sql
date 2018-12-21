# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

The **actual app** is under `app/` with its `app/settings.py`, `app/app.py`
and its configuration in `app/secrets/config.json`.
The build is in `app/Dockerfile`.
For **testing** there is a `testing_app.py`, the actual `pytest` tests
and testdata are under `test/`.
As an example ther is a **build strategy** in `.circleci/config.yml`.

## Testing



**on host**

```
# start actual app
python3 app/app.py
...
# start app with testing endpoints
python3 testing_app.py
...
# run tests
pytest test
```

**dockerized**

```
docker-compose build
docker-compose up -d
docker-compose run tests pytest test
```



# TODO

- properly separate the app from the tests
- deploy startegy
