"""
python manage.py fill_db: fills movies info in database
python manage.py fill_db --first: fills Genres and Movies
"""

from django.core.management.base import BaseCommand, CommandError
from kinopoisk_app.models import Movie, Genre, Actor, Director
import json
from kinopoisk_app.models.Genre import ALL_GENRES


def fill_genres_class():
    for genre in ALL_GENRES:
        if Genre.objects.filter(name=genre).exists():
            continue

        new_genre = Genre.objects.create(name=genre)
        new_genre.save()
    print('Genre is Filled')


# def parse_data(dict_data: dict):
#     res_dict = {}
#     for movie_name, movie_genre in dict_data.items():
#         res_dict[movie_name[movie_name.find('.') + 2:]] = movie_genre
#     return res_dict


def create_movie_objects(dict_data: dict):
    for movie_name, movie_items in dict_data.items():
        genre, director, actor_squad = movie_items
        movie_genre = Genre.objects.get(name=genre)
        director_name, director_lastname = director.split()[:2]
        print(director_name, director_lastname)

        if Director.objects.filter(
                first_name=director_name,
                last_name=director_lastname
        ).exists():
            director_item = Director.objects.get(
                first_name=director_name,
                last_name=director_lastname
            )

        else:
            director_item = Director.objects.create(
                first_name=director_name,
                last_name=director_lastname
            )
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
            parsed_actor_name.append('') if len(parsed_actor_name) == 1 else 0

            # Спросить почему это возвращает None
            # actor_name, actor_lastname = parsed_actor_name.append('') if len(parsed_actor_name) == 1 else parsed_actor_name[:2]

            actor_name, actor_lastname = parsed_actor_name if len(parsed_actor_name) == 1 else parsed_actor_name[:2]
            # print(actor_name, actor_lastname)
            if Actor.objects.filter(first_name=actor_name, last_name=actor_lastname).exists():
                actor = Actor.objects.get(first_name=actor_name, last_name=actor_lastname)
            else:
                actor = Actor.objects.create(first_name=actor_name, last_name=actor_lastname)
                actor.save()
            movie.actor_squad.add(actor)
            movie.save()


movies = open('kinopoisk_app/movies_scrapped_data/movies.json')
# movies_data = parse_data(json.load(movies))
movies_data = json.load(movies)


class Command(BaseCommand):
    help = 'Creates database filling, if iys your first time use --first'

    def add_arguments(self, parser):
        parser.add_argument(
            '--first',
            action='store_true',
            help='Fills Genre table',
        )

    def handle(self, *args, **options):
        if options['first']:
            fill_genres_class()

        create_movie_objects(movies_data)
