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

### Runing the tests
```
docker-compose run --rm django ./manage.py test
```

## Testing environment

You can test the project online at the following URL: `134.209.66.134/graphql`