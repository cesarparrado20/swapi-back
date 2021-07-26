# SW API GraphQL

## Requirements
* [Docker](https://www.python.org/)
* [Docker Compose](https://docs.docker.com/engine/)
* [.EVN](https://docs.docker.com/compose/)

## Setup

Clone the project
```
git clone https://github.com/cesarparrado20/swapi-back.git
```

Example .env
```
SECRET_KEY=g-d^%97w4jgu_+2fzo&io3^tqq71315vv8kv80%%_xm#aqx38g
TZ=America/Bogota
DJANGO_SETTINGS_MODULE=swapi.settings.development

POSTGRES_DB=example-db
POSTGRES_USER=example-user
POSTGRES_PASSWORD=example-pass
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

Create and build services
```
docker-compose build
```

Run migrations and load fixtures
```
docker-compose run --rm django ./manage.py migrate
docker-compose run --rm django ./manage.py load_fixtures
```

### Running the server
```
docker-compose up
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Running the tests
```
docker-compose run --rm django ./manage.py test
```

### Running the logic exercises
```
docker-compose run --rm django python logic_exercises.py
```

## Testing environment

You can test the project online at the following URL: `134.209.66.134/graphql`