### 웹 크롤링 실습 ###

# Wikipedia의 메인 페이지에서 오늘의 주요 기사 제목을 가져오기

import requests
from bs4 import BeautifulSoup

# Wikipedia 메인 페이지의 URL
# Wekipedia > English
url = "https://en.wikipedia.org/wiki/Main_Page"

#! HTTP GET 요청
response = requests.get(url)

#! 요청이 성공했는지 확인
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')

    # 오늘의 주요 기사 제목 선택
    title = soup.select_one('#mp-tfa > p > b > a').text

    print(title)
else:
    print('잘못된 요청입니다.', response.status_code)
    # URL 경로가 잘못된 경우
    # : 잘못된 요청입니다. 404(NOT FOUND)