'''
install selenium
install webdriver-manager
'''
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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

    for position, (movie_name, link) in enumerate(movies_list):
        driver.get(link)
        genre_class = driver.find_elements_by_xpath('//li[@class="ipc-inline-list__item ipc-chip__text"]')
        movies_genres[movie_name] = genre_class[0].text

    with open("movies.json", "w") as outfile:
        json.dump(movies_genres, outfile)


if __name__ == '__main__':
    main()
