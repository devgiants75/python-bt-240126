### 아웃백 스테이크 하우스 웹 페이지의 header 태그 추출 ###
# : 해당 header의 태그와 내용을 추출

# reqeusts 라이브러리
# Beautiful 라이브러리 - bs4 모듈 사용
import requests
from bs4 import BeautifulSoup

url = 'https://www.outback.co.kr/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

id_element = soup.find(id='dHead')
print(id_element) # id가 dHead인 태그 내의 모든 HTML 문서
print(id_element.text) # 해당 HTML 코드 중 내용만 추출

### 네이버 뉴스 헤드라인 크롤링 ###
# 네이버 뉴스 > 원하는 기사를 선택
# > 해당 기사의 원하고자하는 내용을 추출

# BeautifulSoup 객체 메서드 - select()
# : 클래스 또는 아이디 명으로 태그를 찾기
# : BeautifulSoup객체.select('클래스 선택자')
# 클래스 선택자
# - class 속성: .클래스명
# - id 속성: #아이디명

naver_news='https://n.news.naver.com/mnews/article/008/0005000902'
response_news = requests.get(naver_news)
html_news = response_news.text
soup = BeautifulSoup(html_news, 'html.parser')

headlines = soup.select('.media_end_head_title')
print(headlines)
# : select() 메서드는 해당 변수(headline)에 할당된 결과에서
#   각 요소를 리스트로 반환
#   >> 해당 리스트를 순회하면서 텍스트의 내용만 추출
for headline in headlines:
    print(headline.text.strip())
    # 문자열.strip()
    # : 문자열 양끝의 공백과 줄바꿈 제거