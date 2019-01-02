# tl;dr

1. add data model in `app/data/models.py`
2. add namespace under `app/apis/` and register it in `app/app.py`
3. put business logic in `app/data/models.py`

```
python3 app/app.py
...
curl -i -u u1:u1 http://0.0.0.0:5000/posts/
```

# App and Configuration

- see `app/app.py` for namespaces and how app starts up (API namespaces are added here)
- general setting are in `app/settings.py`,
  some are overwritten by `app/secrets/config.json` if it exists
- start with `python3 app/app.py`
- for methods which need app context and should start on app startup
  there is a method in `data/methods.py`
- if there is a `key.pem` and `cert.pem` under `app/secrets/`
  the app starts with SSL
- for more settings see `app/settings.py`: switch `FLASK_DEBUG` on for
  development, off for deploy
- `app/secrets/*` are in `.gitignore`
- database stuff is under `app/data/` (methods, models)
- REST API stuff is under `app/apis/` (endpoints, authentication)

## Edit data

- edit db models in `app/data/models.py`
- the default database URI is `sqlite:///../data/test.db` -- it is shared
  with the `testing_app.py`,
  overwrite by setting `SQLALCHEMY_DATABASE_URI` in `app/secrets/config.json`
- all the querying stuff is under `app/data/methods.py` to keep API logic
  and business logic separated

## Edit apis

- namespaces are registered in `app/app.py`
- add file for new namespace under `app/apis/`
- in namespace file, add enpoints and all that shit;
  if serializer and parsers needed, they also go here
- for the actual data querying use `app/data/methods`,
  so business logic is separated from the pure api stuff

## Authentication

- define authentication method in `app/apis/auth.py`
- use `@auth.login_required` for enpoints
- per default user `u1:u1` is created if there are no users
  defined in `app/secrets/config.json` (see `app/apis/auth.py`)
- if not elaborate enough, put nginx in front of app

## SSL

If `key.pem` and `cert.pem` are found under `app/secrets/`
the app is started with SSL enabled
(`app/secrets/*` are in `.gitignore`).
For testing create self-signed cert as below and put both files
under `app/secrets/`.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 1000
```

Note: Self-signed, so browser will complain.
If this is not enough, put nginx in front of app.
