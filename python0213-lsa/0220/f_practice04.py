### 인터넷 영화 데이터베이스에서 영화 정보 수집 ###
# IMDB: Internet Movie Database
# https://www.imdb.com/

import requests
from bs4 import BeautifulSoup

Movie_URL='https://www.imdb.com/'
headers= {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 영화 데이터 수집 함수
def fetch_movie_data(start):
    url=Movie_URL.format(start)
    response = requests.get(url, headers=headers)
    # HTML 내용에 대한 구문을 분석 (내용만 추출)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    movie_containers = soup.select('.ipc-poster-card ipc-poster-card--baseAlt ipc-poster-card--dynamic-width top-picks-title ipc-sub-grid-item ipc-sub-grid-item--span-2')
    for movie in movie_containers:
        image = movie.div.a
        title = movie.a.span
        print(f'{image} {title}')

fetch_movie_data(0)