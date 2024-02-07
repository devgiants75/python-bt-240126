### 파이썬의 파일 입출력 ###

# 파일 입력: 기존의 파일 내용을 읽어 들이는 것
# 파일 출력: 기존 파일에 새로운 내용을 추가하거나 새로운 파일을 생성하는 것

# 1. 파일 열기
# : 실제로 어떤 파일을 열어보는 것 X
# : 입출력 작업을 진행할 파일을 지정하는 것
# : 입력과 출력 모두 파일 열기 작업을 가장 먼저 수행해야 함

# : open()함수 사용 - 파일 객체를 반환
# 파일 객체 = open(파일명, 모드)

# 1. 파일명: 입출력을 수행할 파일
# 1) 파일명만 작성하는 경우
# : 파이썬 소스 코드 파일(.py)과 동일한 경로에 존재하는 파일
# ex) open('sample.txt')

# 2) 전체 경로를 지정하는 경우
# : 파일이 다른 디렉터리(폴더)에 있는 경우 지정
# ex) 'C:\\python0126-lsa\\sample.txt'

# 3) 상대 경로 - 현재 디렉터리를 기준으로 경로 지정(./)
# : 해당 파일이 같은 디렉터리 폴더 안에 있는 경우

# 4) 상위 디렉터리를 기준으로 경로 지정(../)

# 2. 모드: 파일을 여는 목적
# 입력 r (read, 읽기) - 파일이 없을 경우(오류), 파일이 있는 경우(읽기)
# >> 입출력 모드를 생략하는 경우 기본으로 r 모드로 파일이 열림

# 출력 w, a, x
# w (write, 쓰기): 파일이 없을 경우(새로 생성), 파일이 있는 경우(새로 생성)
# a (append, 추가): 파일이 없을 경우(새로 생성), 파일이 있는 경우(추가)
# x (exclusive, 배타적 추가): 파일 X(새로 생성), 파일 O(오류)

# 3. 파일의 종류
# 텍스트 파일 OR 바이너리 파일(텍스트 파일을 제외한 모든 파일)
# t(text): 텍스트 파일 (파일 종류 생략 시 기본적으로 t모드 파일 열림)
# b(binary): 바이너리 파일

# 모드와 파일의 종류 혼합
# rt: 텍스트 파일 읽기 모드
# ab: 바이너리 파일 추가 모드

#! 파일 닫기
# : close() 함수 사용
# 파일객체.close()

file = open('new_file.txt', 'wt') # 새 파일 생성
file.close()

#! with문
# : 파일을 열고 작업을 마친 후 자동으로 파일을 닫아주는 기능
# : close()함수를 따로 사용하지 않아도 가능

# with open('파일명', '모드) as file객체명:
#   파일 처리 코드

with open('my_file.txt', 'wt') as file:
    print('my_file.txt 파일이 생성되었습니다.')

### 파이썬 파일 출력 ###

# 1. (텍스트 파일) 생성
file = open('file_output.txt', 'wt')
# write()함수를 사용하여 파일에 내용을 작성
file.write('Hello, this is a sample text file')
file.close()

# 2. (텍스트 파일) 내용 추가하기
file = open('file_output.txt', 'a')
file.write('\n') # \n: 줄바꿈
file.write('This is additional text!')
file.close()

### 파일 입력(input) ###
# r(read, 읽기)모드를 사용하여 파일 열기
# read() 함수 사용

# 인코딩
# : 문자나 기호들을 컴퓨터에 저장하거나 전송할 수 있는 형태로 변환하는 과정
# : 즉, 0과 1(이진 데이터)로 변환하는 규칙
# : UTF-8(유니코드 인코딩 방식) 사용을 권장
# >> open함수에 encoding='' 속성을 추가

file = open('my_file.txt', 'a')
file.write('Hello')
file.close()

# utf-8 지정 시 글자 작성은 영어로 작성
file = open('my_file.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()

# 파일의 여러 줄을 읽어오는 경우 readline()함수를 사용
# : 각 줄 마다 반복해야 함 >> while반복문

file = open('my_file.txt', 'a')
file.write('\n')
file.write('nice to meet you')
file.close()

file = open('my_file.txt', 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line: break
    print(line)
file.close()

with open('my_file.txt', 'rt') as file:
    content = file.read()
    print(content)

print('--모든 줄을 리스트로 읽기--')
# 모든 줄을 리스트로 읽기
# : readlines() 함수: 파일의 각 줄을 요소로 하는 리스트를 반환
file = open('my_file.txt', 'r', encoding='utf-8')
lines = file.readlines() # lines: 리스트
for line in lines:
    print(line)
file.close()

print(lines)

