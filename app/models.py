from django.db import models
from model_utils.models import TimeStampedModel


class SimpleNameModel(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Planet(TimeStampedModel, SimpleNameModel):
    """ Planetas del universo de Star Wars """

    rotation_period = models.CharField(max_length=40, blank=True)
    orbital_period = models.CharField(max_length=40, blank=True)
    diameter = models.CharField(max_length=40, blank=True)
    climate = models.CharField(max_length=40, blank=True)
    gravity = models.CharField(max_length=40, blank=True)
    terrain = models.CharField(max_length=40, blank=True)
    surface_water = models.CharField(max_length=40, blank=True)
    population = models.CharField(max_length=40, blank=True)

    class Meta:
        db_table = 'planet'


class People(TimeStampedModel, SimpleNameModel):
    """ Personajes del universo de Star Wars """
    MALE = 'male'
    FEMALE = 'female'
    HERMAPHRODITE = 'hermaphrodite'
    NA = 'n/a'

    BLACK_HAIR = 'BLACK'
    BROWN_HAIR = 'BROWN'
    BLONDE_HAIR = 'BLONDE'
    RED_HAIR = 'RED'
    WHITE_HAIR = 'WHITE'
    BALD_HAIR = 'BALD'

    BLACK_EYE = 'BLACK'
    BROWN_EYE = 'BROWN'
    YELLOW_EYE = 'YELLOW'
    RED_EYE = 'RED'
    GREEN_EYE = 'GREEN'
    PURPLE_EYE = 'PURPLE'
    UNKNOWN_EYE = 'UNKNOWN'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (HERMAPHRODITE, 'Hermaphrodite'),
        (NA, 'N/A'),
    )

    HAIR_COLORS = (
        (BLACK_HAIR, 'BLACK'),
        (BROWN_HAIR, 'BROWN'),
        (BLONDE_HAIR, 'BLONDE'),
        (RED_HAIR, 'RED'),
        (WHITE_HAIR, 'WHITE'),
        (BALD_HAIR, 'BALD')
    )

    EYE_COLORS = (
        (BLACK_EYE, 'BLACK'),
        (BROWN_EYE, 'BROWN'),
        (YELLOW_EYE, 'YELLOW'),
        (RED_EYE, 'RED'),
        (GREEN_EYE, 'GREEN'),
        (PURPLE_EYE, 'PURPLE'),
        (UNKNOWN_EYE, 'UNKNOWN')
    )

    height = models.CharField(max_length=16, blank=True)
    mass = models.CharField(max_length=16, blank=True)
    hair_color = models.CharField(
        max_length=32, choices=HAIR_COLORS, default=BLACK_HAIR
    )
    skin_color = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(
        max_length=32, choices=EYE_COLORS, default=UNKNOWN_EYE
    )
    birth_year = models.CharField(max_length=16, blank=True)
    gender = models.CharField(max_length=64, choices=GENDER)
    home_world = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name='inhabitants'
    )

    class Meta:
        db_table = 'people'
        verbose_name_plural = 'people'


class Director(SimpleNameModel):
    """ Directores de películas"""

    class Meta:
        db_table = 'director'


class Producer(SimpleNameModel):
    """ Productores de películas"""

    class Meta:
        db_table = 'producer'


class Film(TimeStampedModel):
    EPISODES_ONE = 1
    EPISODES_TWO = 2
    EPISODES_THREE = 3
    EPISODES_FOUR = 4
    EPISODES_FIVE = 5

    EPISODES = (
        (EPISODES_ONE, 'Episodio 1'),
        (EPISODES_TWO, 'Episodio 2'),
        (EPISODES_THREE, 'Episodio 3'),
        (EPISODES_FOUR, 'Episodio 4'),
        (EPISODES_FIVE, 'Episodio 5')
    )

    title = models.CharField(max_length=100)
    episode_id = models.PositiveSmallIntegerField(choices=EPISODES)
    opening_crawl = models.TextField(max_length=1000)
    release_date = models.DateField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name='films'
    )
    producer = models.ManyToManyField(Producer, related_name='films')
    characters = models.ManyToManyField(
        People, related_name='films', blank=True
    )
    planets = models.ManyToManyField(Planet, related_name='films', blank=True)

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title
