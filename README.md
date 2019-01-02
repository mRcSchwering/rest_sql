# tl;dr

```
python3 app/app.py
curl -i -u u1:u1 http://0.0.0.0:5000/posts/
```

# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

The **actual app** is under `app/` with its `app/settings.py`, `app/app.py`
and its configuration in `app/secrets/config.json`.
The build is in `app/Dockerfile`.
For **testing** there is a `testing_app.py`, the actual `pytest` tests
are under `test/`.
As an example ther is a **build strategy** in `.circleci/config.yml`.

## Testing

The default database URIs for both apps make sense for testing.
`app/app.py` and the `testing_app.py`
share the test database in `data/test.db` (see `docker-compose.yml`).
Like this integration tests work both dockerized and locally.

**local**

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
docker-compose exec tests pytest test
```

# TODO

- deploy startegy.
