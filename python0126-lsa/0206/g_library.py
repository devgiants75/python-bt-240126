# 파이썬 표준 라이브러리

#! 라이브러리
# : 파이썬 설치 패키지에 포함되어 있는
# : 여러 기능을 제공하는 모듈과 패키지의 집합

#! 표준 라이브러리 종류
# math: 수학적 함수, 상수 제공
# datetime: 날짜와 시간을 조작하는 기능을 제공
# random: 랜덤 숫자 생성 기능을 제공
# os: 운영체제와 상호 작용하는 기능을 제공

#! math 모듈
import math

# 1. 상수 사용
# math.pi: 파이 - 원주율
print(math.pi) # 3.141592653...

# 2. 제곱근 함수 사용
# math.sqrt(n)
print(math.sqrt(16)) # 4.0

# math 모듈의 함수들은 부동 소수점 수를 반환
# : 정수를 입력하더라도 무조건 소수점 자리를 반환
# 4 > 4.0, 17 > 17.0

# 기타 수학 함수
# math.fabs(): 절댓값
# math.factorial: 팩토리얼(!)
# math.ceil: 올림
# math.floor: 내림

print(math.fabs(-5)) # 5.0
print(math.factorial(5)) # 120
print(math.ceil(2.3)) # 3
print(math.floor(2.7)) # 2

#! datetime 모듈
# : 날짜와 시간을 처리하는 기능

import datetime

# 현재 날짜 및 시간을 가져오기
now = datetime.datetime.now()
print(now)

# 날짜, 시간의 형식 지정
# date(날짜)
date = datetime.date(2024, 2, 6)
print(date) # 2024-02-06

# time(시간)
time = datetime.time(11, 8, 10)
print(time) # 11:08:10

# datetime 모듈의 주요 메서드
# : 오늘 날짜 / 현재 날짜와 시간을 반환
print(datetime.date.today())
print(datetime.datetime.now())

#! os 모듈
# : operate system (운영체제)와 상호작용하는 기능
import os

# 현재 작업 디렉터리(폴더) 확인
# cwd: current workspace directory
print(os.getcwd()) # C:\python-workspace\python0126-lsa\0206

# 디렉터리(폴더) 생성
# mkdir: make directory
# os.mkdir('practice') >> 한 번 생성한 폴더를 재생성 불가

# 디렉터리 확인
print(os.listdir)

# 디렉터리 삭제
# : 삭제하려는 디렉터리가 존재하지 않을 경우 오류 발생
# rmdir: remove directory
# os.rmdir('practice') >> 존재하지 않는 폴더 삭제 시 오류

#! random 모듈
# : 난수를 생성하는 기능을 제공
# : 임의의 수를 생성하거나, 시퀀스를 무작위로 섞는 등의 작업을 수행

import random

# 난수 생성

# random()
# 0.0과 1.0 사이의 실수, 매개변수 X
print(random.random())

# uniform(a, b)
# : 지정된 두 값 a, b 사이의 실수를 생성
print(random.uniform(1, 10))

# randint(a, b)
# : 지정된 두 값 a, b 사이의 정수를 생성
print(random.randint(1, 10))

# 시퀀스 관련 함수 사용
my_list = [1, 2, 3, 4, 5]
random_my_list = random.choice(my_list)
print(random_my_list)

random.shuffle(my_list)
print(my_list)