### 인터넷 영화 데이터베이스에서 영화 정보 수집 ###
# IMDB: Internet Movie Database
# https://www.imdb.com/

import requests
from bs4 import BeautifulSoup

# 영화 목록 페이지의 실제 URL로 변경
Movie_URL = 'https://www.imdb.com/path/to/movie/list'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


# 영화 데이터 수집 함수
def fetch_movie_data():
    response = requests.get(Movie_URL, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    # 영화 컨테이너 선택자를 확인하고 수정
    movie_containers = soup.find_all('div', class_='your-correct-class-here')

    for movie in movie_containers:
        # 이미지와 제목을 추출하는 올바른 방법으로 변경
        image = movie.find('img')['src']
        title = movie.find('a')['title']
        print(f'Image URL: {image}, Title: {title}')


fetch_movie_data()
