### 검색 결과 웹 페이지 정보 가져오기 예제 실습 ###
import requests

# 롯데 자이언츠 경기 일정 페이지의 정보를 가져오기
# : https://www.giantsclub.com/html/?pcode=257

# 롯데 자이언츠 기본 URL
base_url = 'https://www.giantsclub.com/html/'

# URL 파라미터 설정
params = {'pcode': '257'}

# User-Agent 설정
# : 웹 서버의 차단을 피하기 위해 설정
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

response = requests.get(base_url, params=params, headers=headers)

# 조건문을 활용한 상태 코드 관리
if response.status_code == 200:
    print(response.text)
else:
    print(f'Error: {response.status_code}: Unable to fetch the webpage')