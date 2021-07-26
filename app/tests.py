import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import from_global_id, to_global_id

from app.models import Planet, People
from swapi.schema import schema


class QueryTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_planet_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPeople {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPeople']['edges']), 84)

    def test_film_query(self):
        response = self.query(
            '''
                query{
                  allFilms {
                    edges{
                      node{
                        id
                        title
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allFilms']['edges']), 12)

    def test_director_query(self):
        response = self.query(
            '''
                query{
                  allDirectors {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allDirectors']['edges']), 5)

    def test_producer_query(self):
        response = self.query(
            '''
                query{
                  allProducers {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allProducers']['edges']), 6)


class MutationTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_add_planet(self):
        response = self.query(
            '''
            mutation addPlanet ($input: AddOrUpdatePlanetMutationInput!) {
                addOrUpdatePlanet (input: $input) {
                    planet {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='addPlanet',
            input_data={'name': 'planet in test'}
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        planet_id = content['data']['addOrUpdatePlanet']['planet']['id']
        planet_id = from_global_id(planet_id)[1]
        self.assertEqual(Planet.objects.filter(id=planet_id).exists(), True)

    def test_update_planet(self):
        planet = Planet.objects.create(name='planet in test')
        response = self.query(
            '''
            mutation updatePlanet ($input: AddOrUpdatePlanetMutationInput!) {
                addOrUpdatePlanet (input: $input) {
                    planet {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='updatePlanet',
            input_data={
                'id': to_global_id('Planet', planet.id),
                'name': 'planet in test - updated'
            }
        )
        self.assertResponseNoErrors(response)
        planet = Planet.objects.get(id=planet.id)
        self.assertEqual(planet.name, 'planet in test - updated')

    def test_add_people(self):
        planet = Planet.objects.create(name='planet in test')
        planet_id = to_global_id('Planet', planet.id)
        response = self.query(
            '''
            mutation addPeople ($input: AddOrUpdatePeopleMutationInput!) {
                addOrUpdatePeople (input: $input) {
                    people {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='addPeople',
            input_data={'name': 'people in test', 'homeWorld': planet_id}
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        people_id = content['data']['addOrUpdatePeople']['people']['id']
        people_id = from_global_id(people_id)[1]
        self.assertEqual(People.objects.filter(id=people_id).exists(), True)

    def test_update_people(self):
        planet = Planet.objects.create(name='planet in test')
        planet_id = to_global_id('Planet', planet.id)
        people = People.objects.create(
            name='people in test', home_world=planet
        )
        response = self.query(
            '''
            mutation updatePeople ($input: AddOrUpdatePeopleMutationInput!) {
                addOrUpdatePeople (input: $input) {
                    people {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='updatePeople',
            input_data={
                'id': to_global_id('People', people.id),
                'homeWorld': planet_id,
                'name': 'people in test - updated'
            }
        )
        self.assertResponseNoErrors(response)
        people = People.objects.get(id=people.id)
        self.assertEqual(people.name, 'people in test - updated')
