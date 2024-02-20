### 아웃백 스테이크 하우스 웹 페이지의 header 태그 추출 ###
# : 해당 header의 태그와 내용을 추출

# reqeusts 라이브러리
# Beautiful 라이브러리 - bs4 모듈 사용

### 네이버 뉴스 헤드라인 크롤링 ###
# 네이버 뉴스 > 원하는 기사를 선택
# > 해당 기사의 원하고자하는 내용을 추출

# BeautifulSoup 객체 메서드 - select()
# : 클래스 또는 아이디 명으로 태그를 찾기
# : BeautifulSoup객체.select('클래스 선택자')
# 클래스 선택자
# - class 속성: .클래스명
# - id 속성: #아이디명