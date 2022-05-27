from django.core.management.base import BaseCommand, CommandError
from kinopoisk_app.models import Movie, Genre, Actor, Director
import json
from pprint import pprint
from kinopoisk_app.models.Genre import ALL_GENRES


def fill_genres_class():
    for genre in ALL_GENRES:
        new_genre = Genre.objects.create(name=genre)
        new_genre.save()


def parse_data(dict_data: dict):
    res_dict = {}
    for movie_name, movie_genre in dict_data.items():
        res_dict[movie_name[movie_name.find('.') + 2:]] = movie_genre
    return res_dict


def create_movie_objects(dict_data: dict):
    for movie_name, movie_items in dict_data.items():
        print(movie_items)
        genre, director, actor_squad = movie_items
        movie_genre = Genre.objects.get(name=genre)
        director_name, director_lastname = director.split()[:2]

        if Director.objects.filter(
                first_name=director_name,
                last_name=director_lastname
        ).exists():
            director_item = Director.objects.get(
                first_name=director_name,
                last_name=director_lastname
            )

        else:
            director_item = Director.objects.create()
            director_item.save()

        if Movie.objects.filter(
                name=movie_name
        ).exists():
            continue

        else:
            movie = Movie.objects.create(
                name=movie_name,
                genre=movie_genre, film_director=director_item)
            movie.save()

        for actor_fullname in actor_squad:
            parsed_actor_name = actor_fullname.split()
            actor_name, actor_lastname = parsed_actor_name, '' if len(parsed_actor_name) == 1 else parsed_actor_name[:2]
            print(actor_name, actor_lastname)
            # actor_name, actor_lastname = parsed_actor_name[:2]
            if Actor.objects.filter(first_name=actor_name, last_name=actor_lastname).exists():
                actor = Actor.objects.get(first_name=actor_name, last_name=actor_lastname)
            else:
                actor = Actor.objects.create(first_name=actor_name, last_name=actor_lastname)
                actor.save()
            movie.actor_squad.add(actor)
            movie.save()


movies = open('kinopoisk_app/movies_scrapped_data/movies.json')
movies_data = parse_data(json.load(movies))


class Command(BaseCommand):
    help = 'Creates database filling'

    def handle(self, *args, **options):
        # fill_genres_class()
        create_movie_objects(movies_data)
