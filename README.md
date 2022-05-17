# kinopoisk via DRF
## Pet-project with kinopoisk features
Конечной целью проектирования БД является создание системы «Кинопоиск», способной оказывать информационные услуги 
по выдаче необходимых данных и их обновлению. БД содержит информацию о фильмах, актерах, режиссерах, пользователях,  
о кинозалах, в которых демонстрируются эти фильмы, и  обеспечивает возможность поиска и отбора данных, 
а также позволяет формировать рейтинг фильмов.
В соответствии с предметной областью система строится с учётом следующих особенностей:
- каждый фильм представлен в рамках своего жанра;
- для каждого фильма можно получить информацию об его режиссере и участвующих актерах;
- у каждого  режиссера есть своя фильмография;
- каждый актер может сниматься  в нескольких фильмах;
- по отзывам, оставленным пользователями, формируется рейтинг фильма;
- каждый фильм может демонстрироваться в нескольких кинозалах;
- в афише кинозала может быть указано несколько фильмов.

![Kinopoisk_db drawio](https://user-images.githubusercontent.com/57236252/168787203-f0ed4359-ceb3-49dc-9d89-cd7d30e508f9.svg)
