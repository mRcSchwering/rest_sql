# TODO

- docker-compose for tests

# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

## App configuration and start

- see `app.py` for namespaces and how app starts up (API namespaces are added here)
- general setting are in `settings.py`, some are loaded from `secrets/config.json`
  if it exists
- for methods which need app context and should start on app startup
  there is a method in `data/methods.py`
- depending on files under `secrets/` the app starts without SSL and in
  flask debug mode (see **SSL** and **Tests**)
- `secrets/*` are in `.gitignore`

Start app with:

```
python3 app.py
```

## Edit data

- edit models in `data/models.py`
- add them to _reset db method_ in `apis/misc.py` so that they are actually created
  (if there should be a reset method)

## Edit apis

- add file for new namespace under `apis/`
- register new namespace in `app.py`
- edit namespace file, add enpoints and all that shit;
  if serializer and parsers needed, they also go here
- for the actual data querying use `data/methods`, so business logic is separated
  from the pure api stuff

## Authentication

- define authentication method in `apis/auth.py`
- use `@auth.login_required` for enpoints
- per default user `u1:u1` is created if there are no users
  defined in `secrets/config.json`

## Tests

- when app starts and there is no `config.json` under `secrets`
  with a `SQLALCHEMY_DATABASE_URI` key, `TESTING` is set
  (see `settings.py`).
- it switches off `SSL` and sets `sqlite:///:memory:` as database URI
- Flask debug mode is also switched off and logging set to _INFO_
- A `/reset_testdata/` endpoint is added to the api,
  which would normally not be added (see `app.py`).

**Hints**

```
curl -i -u u1:asd \
  http://0.0.0.0:5000/posts?id=1

curl -i -u u1:asd \
  http://0.0.0.0:5000/posts/

curl -i -u u1:asd \
  -H "Content-Type: application/json" \
  -d '{"title": "my post", "body": "asdf", "category_id": 1}' \
  http://0.0.0.0:5000/posts/
```

## SSL

Create self-signed cert as below and put both files
`key.pem` and `cert.pem` under `secrets/`.
If these files are found SSL will be enabled in settings automatically.
For testing SSL will be switched off.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 1000
```

Self-signed, so browser will complain.

## Docker

Hosts in app (`settings.FLASK_SERVER_NAME`) needs to be `0.0.0.0`.

```
docker build -t flask_app .
docker run --rm -p 5000:5000 flask_app
```

# to document

- on app startup in methods called in app
- testdatabase in test/testdata
- settings, overwritten if appropriate files there
- auth u1, u1 if TESTING, sonst in json
