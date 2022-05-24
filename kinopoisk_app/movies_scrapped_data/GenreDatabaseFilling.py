from kinopoisk_app.models.Genre import Genre
from kinopoisk_app.models.Genre import ALL_GENRES


def fill_genres_class():
    for genre in ALL_GENRES:
        new_genre = Genre.objects.create(name=genre)
        new_genre.save()


if __name__ == '__main__':
    fill_genres_class()
