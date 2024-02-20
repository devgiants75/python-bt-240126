### 영화 예매 사이트 정보 추출 ###
import requests
from bs4 import BeautifulSoup

## 보안에 따른 접근방지: 코드의 결과 확인이 불가 ##

url='https://www.cgv.co.kr/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# CGV 영화 예매 사이트
# : 메인 페이지 무비 차트의 영화 제목을 가져오기

class_elements = soup.find_all('div', class_='movieName')
for element in class_elements:
    print(element.text)