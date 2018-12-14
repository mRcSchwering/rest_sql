## Edit data

- edit models in `data/models.py`
- add them to _reset db method_ in `apis/misc.py` so that they are actually created


## Edit apis

- add file for new namespace under `apis/`
- register new namespace in `app.py`
- edit namespace file, add enpoints (`@api.route()`) and all that shit
- if serializer needed, add to `apis/serializers.py`

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
