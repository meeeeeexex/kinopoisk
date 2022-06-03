from kinopoisk_app.models.common.Person import Person


class Director(Person):

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
