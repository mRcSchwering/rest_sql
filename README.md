# tl;dr

```
pip3 install -r app/requirements.txt
python3 app/app.py
curl -i -u u1:u1 http://0.0.0.0:5000/posts
```


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
docker-compose exec tests pytest test
```



# TODO

- mit DB `sqlite:///test/test.db` geht dockerized nicht mehr.
  docker container müssten beide ein volume for test.db sharen
- deploy startegy.
