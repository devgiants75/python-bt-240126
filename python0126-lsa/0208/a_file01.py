# 파이썬 - 파일 입출력

#! 파일 열기: open(파일명, 모드, 인코딩)함수
# 파일명: 입출력을 작업을 수행할 파일

# 1. 파일명만 작성하는 경우
# : 파이썬 소스 코드 파일(.py)과 동일한 경로에 존재하는 파일
# ex) open('sample.txt')

# 2. 전체 경로를 지정하는 경우: 절대 경로
# : 파일 시스템에서의 전체 경로를 의미
# : 루트 디렉토리(폴더)부터 시작하여 파일의 위치한 곳까지 전체 지정
# : 파일 경로의 구분자는 역슬래시(\)
file = open('C:\\이승아\\python-workspace\\path.txt', 'rt', encoding='utf-8')
content = file.read()
print(content)
file.close()
# 모드
# r: 읽기
# w: 쓰기, a: 추가, x: 배타적 추가

# 이스케이프 코드
# : 프로그래밍을 할 때 사용할 수 있도록 미리 정의해 둔 문자 조합
# : 일반적인 문법과의 충돌을 막기 위한 용도
# \n: 줄바꿈(개행)
# \", \': 큰(작은) 따옴표 출력
# \\: 실제 역슬래시 자체를 표현
print("\"안녕하세요\"")

# 현재 디렉터리(폴더)를 기준으로 경로를 지정: ./
# : 해당 파일이 같은 디렉터리 폴더에 존재하는 경우
# : 파일명만 작성하는 경우와 동일한 환경
file = open('./path.txt', 'rt', encoding='utf-8')
lines = file.readlines() # lines 리스트
for line in lines:
    print(line)
file.close()

# 상위 디렉터리를 기준으로 경로 지정: ../
# : 폴더를 벗어나는 방법
file = open('../path.txt', 'rt', encoding='utf-8')
while True:
    line = file.readline()
    if not line: break
    print(line)
file.close()

file = open('../../abc.txt', 'rt', encoding='utf-8')
content = file.read()
print(content)
file.close()