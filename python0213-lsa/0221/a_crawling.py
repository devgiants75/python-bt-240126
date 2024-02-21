### 웹 크롤링 예제 ###

# 네이버 스포츠 페이지에서 특정 정보를 추출하는 예시

# 0. 필요한 라이브러리 임포트
import requests
from bs4 import BeautifulSoup

# 1. 네이버 스포츠 페이지의 구조를 가져오기 (requests)
url = 'https://sports.news.naver.com/index.nhn'

response = requests.get(url)

# requests 응답 내용 중 HTML 부분을 문자열로 가져오기
html = response.text

# 2. 가져온 구조에서 특정 정보를 추출 (BeautifulSoup - bs4)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 중복된 class 속성의 지정된 영역을 가져오기

# li태그 (class 속성 - today_item)
list_items = soup.find_all('li', class_='today_item')

# 원하는 데이터 추출
# : class 속성이 title인 요소를 가져오기
titles = [
    # 가져온 title 요소에서 텍스트의 공백을 없애고
    # : 내용만 추출
    item.find(class_='title').get_text(strip=True)
    # list_items 요소 내에서 class가 title인 하위 요소 찾기
    # : for 반복을 통해 각각의 요소를 item에 전달
    for item in list_items if item.find(class_='title')
]

# titles 리스트의 각 요소를 순회하며 출력
for title in titles:
    print(title)