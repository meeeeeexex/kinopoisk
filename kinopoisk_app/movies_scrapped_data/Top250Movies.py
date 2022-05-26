'''
install selenium
install webdriver-manager
'''
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

''''
ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link
ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'''


def parse_data(dict_data: dict):
    res_dict = {}
    for movie_name, movie_genre in dict_data.items():
        res_dict[movie_name[movie_name.find('.') + 2:]] = movie_genre
    return res_dict


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    movies = driver.find_elements_by_xpath('//td[@class="titleColumn"]')
    movies_list = []
    for movie in movies:
        movie_name = movie.text
        movie_link = movie.find_element_by_css_selector('a').get_attribute('href')
        movies_list.append((movie_name, movie_link))

    movies_genres = {}
    directors_dict = {}

    for position, (movie_name, link) in enumerate(movies_list):
        driver.get(link)
        genre_class = driver.find_elements_by_xpath('//li[@class="ipc-inline-list__item ipc-chip__text"]')
        actors = driver.find_elements_by_xpath(
            '//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]')
        actor_squad = []
        for actor in actors:
            if actor.text == '':
                break
            actor_squad.append(actor.text)
        movies_genres[movie_name] = (genre_class[0].text, actor_squad[0], actor_squad[1:])
        print(movies_genres)

    movies_dict = parse_data(movies_genres)

    with open("movies.json", "w") as outfile:
        json.dump(movies_dict, outfile)


if __name__ == '__main__':
    main()
