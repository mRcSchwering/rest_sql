# REST-SQL

Personal boilerplate code for REST API using Flask and SQLalchemy.
Because I will forget it anyway..

## App configuration and start

- see `app.py` for namespaces and how app starts up
- general setting are in `settings.py`

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

## Test with curl

```
curl -i -u u1:asd \
  http://localhost:5000/posts?id=1

curl -i -u u1:asd \
  http://localhost:5000/posts/

curl -i -u u1:asd \
  -H "Content-Type: application/json" \
  -d -d '{"title": "my post", "body": "asdf", "category_id": 1}' \
  http://localhost:5000/posts/
```

## SSL

Create self-signed cert as below and put both files under `certs/`.
Then enable ssl in `settings.py`.
The browser will still complain though.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 1000
```
