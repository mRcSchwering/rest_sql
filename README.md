## Edit data

- edit models in `data/models.py`
- add them to _reset db method_ in `apis/misc.py` so that they are actually created
  (if there should be a reset method)


## Edit apis

- add file for new namespace under `apis/`
- register new namespace in `app.py`
- edit namespace file, add enpoints (`@api.route()`) and all that shit;
  if serializer and parsers needed, they also go here
- for the actual data querying use `data/methods`, so business logic is separated
  from the pure api stuff

## App configuration

- see `app.py`
- some stuff is in `settings.py`

## Start app

```
python3 app.py
```

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
