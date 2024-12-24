# Tutorial 1: Serialization

## Reference

- https://www.django-rest-framework.org/tutorial/1-serialization/

## pyenv

```sh
pyenv install 3.12.3
pyenv global 3.12.3
```

## poetry

```sh
python -m pip install poetry
python -m poetry shell
```

## Install packages

```sh
poetry install
```

## ruff

```sh
python -m ruff format
python -m ruff check --fix
```

## Run migrations

```sh
python manage.py migrate
```

## Run server

```sh
python manage.py runserver
```

## curl

### Snippet list

```sh
curl --location '127.0.0.1:8000/snippets/'
```

### Snippet create

```sh
curl --location '127.0.0.1:8000/snippets/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "New Snippet",
    "code": "print('\''hello world'\'')",
    "linenos": true,
    "language": "python",
    "style": "friendly"
}
'
```

### Snippet detail

```sh
curl --location '127.0.0.1:8000/snippets/1/'
```
