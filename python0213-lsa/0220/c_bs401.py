### 웹 페이지 분석 및 추출하기 ###

#! BeautifulSoup
# : 웹 페이지의 HTML 코드를 파싱(분석)하여 데이터를 추출하는 라이브러리

#! 1. BeatifulSoup 객체 생성 기본 방법

# BeautifulSoup 객체를 생성하기 위해서는
# , 먼저 웹 페이지의 HTML 코드를 가져와야 한다. (reqeusts)
import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=257'

response = requests.get(url)
# reqeusts로 가져오는 정보를 response에 저장
# response 내에는 해당 요청에 대한 상태 코드와 결과값이 담겨있다.
html = response.text # 요청 결과 (HTML 코드)

#! 1. BeautifulSoup 객체 생성
# 'html.parser'는 파싱(분석)에 사용할 파서를 지정
soup = BeautifulSoup(html, 'html.parser')

#! 2. BeautifulSoup 메서드 사용
# BeautifulSoup 객체는 태그 검색
# , 접근 & 데이터 추출에 대한 다양한 메서드를 제공

# a. find() 메서드
# : 특정 태그들 중에서 가장 첫 번째 태그만 가져오는 메서드
# : 일반적으로 하나의 태그만 존재하는 경우 사용
a_tag = soup.find('a')
# 태그의 내용 반환 soup.find('태그명').text
print(a_tag.text)

# 태그의 속성에 접근 soup.find('태그명').get('속성명')
a_tag_href = soup.find('a').get('href')
print(a_tag_href) # #inner_nav

# b. find_all()메서드
# : 조건에 맞는 모든 태그를 찾는 데 사용
# : 가져온 태그들은 모두 리스트의 요소로 저장 (리스트 형태로 반환)

# 태그: soup.find_all('태그명')
# 태그 내용: soup.find_all('태그명')[가져올내용의인덱스번호].text
# 태그 속성값: soup.find_all('태그명')[인덱스번호].get('속성명')

span_tag = soup.find_all('span')
for tag in span_tag:
    print(tag.text)

# c. class 속성 활용
# : 공통적인 특징을 갖는 태그들은 같은 class 속성값으로 묶을 수 있다.
# : 공통된 내용에 하나의 이름표를 붙임
# : find(), find_all() 메서드 모두 동일하게 사용 가능
#   클래스 이름으로 요소를 찾을 때: 'class_' 파라미터를 사용

class_elements = soup.find_all(class_='top_menu')
print('clss 속성 사용 - top menu')
for element in class_elements:
    print(element.text)

# d. id 속성 활용
# : 같은 웹 페이지에서 같은 id 속성값을 가진 태그는 존재하지 X
# : 특정 id 속성값을 가진 태그는 오직 하나
# : find 메서드와 함께 사용

# 태그: soup.find('태그명', id='id속성값')
# 태그 내용: soup.find('태그명', id='속성값').text
# : id 파라미터 사용
id_element = soup.find(id='skipArea')
print(id_element)
print(id_element.text)