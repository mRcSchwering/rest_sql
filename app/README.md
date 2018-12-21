# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

## App configuration and start

- see `app.py` for namespaces and how app starts up (API namespaces are added here)
- general setting are in `settings.py`, some are loaded from `secrets/config.json`
  if it exists
- start with `python app.py`; `python app.py test` for testing
- testing disables ssl, adds a enpoint for resetting testdata,
  and switches on flask dbug
- for methods which need app context and should start on app startup
  there is a method in `data/methods.py`
- depending on files under `secrets/` the app starts with SSL and in
  flask debug mode (see **SSL** and **Tests**)
- `secrets/*` are in `.gitignore`

## Edit data

- edit models in `data/models.py`
- add them to _reset db method_ in `apis/misc.py` so that they are actually created
  (if there should be a reset method)
- the default database URI is `sqlite:///:memory:`,
  it can be overwritten by setting `SQLALCHEMY_DATABASE_URI` in `secrets/config.json`

## Edit apis

- add file for new namespace under `apis/`
- register new namespace in `app.py`
- edit namespace file, add enpoints and all that shit;
  if serializer and parsers needed, they also go here
- for the actual data querying use `data/methods`, so business logic is separated
  from the pure api stuff
- when app starts in test mode the `apis/reset_testdata.py` is added
  (see `app.py`)

## Authentication

- define authentication method in `apis/auth.py`
- use `@auth.login_required` for enpoints
- per default user `u1:u1` is created if there are no users
  defined in `secrets/config.json` (see `test/utils.py`)

## Tests

- start app with `python app.py test` for testing
- it switches off `SSL`
- Flask debug mode is also switched on and logging set to _DEBUG_
- A `/reset_testdata/` endpoint is added to the api,
  which would normally not be added (see `app.py`).

## SSL

Create self-signed cert as below and put both files
`key.pem` and `cert.pem` under `secrets/`.
If these files are found SSL will be enabled in settings automatically.
In test mode SSL is always switched off.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 1000
```

Self-signed, so browser will complain.

## Docker

- `Dockerfile` includes the whole repo, also `test/*`
- `docker-compose.yml` for running app in 1 container, and testing from another

## Build

- there is a build procedure under `.circleci/`
- see `.circleci/config.yml`

# TODO

- properly separate the app from the tests
- deploy startegy
