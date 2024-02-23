### 파이썬에서 엑셀 파일 다루기 ###

# Pandas & Openpyxl 외부 라이브러리
# 1. Pandas
# : 데이터 분석을 위한 고수준의 자료 구조와 데이터 분석 도구를 제공

# 2. Openpyxl
# : Excel(.xlsx)파일을 읽고 쓰기 위한 도구를 제공

# 설치 명령어
# pip install pandas
# pip install openpyxl

#! Pandas 라이브러리 활용
# : python 데이터 분석 라이브러리
# : 구조화된 데이터를 효율적으로 처리하고 분석

# 1. Pandas의 주요 구성 요소 (Series, DataFrame)
# Series: 1차원 레이블이 지정된 배열 (단일 데이터 값 포함)
# - 각각의 데이터는 인덱스 번호를 가짐
# - 기본 생성 예제
import pandas as pd

data = pd.Series([1, 3, 5, 7, 9])
print(data)

# Series는 기본적으로 0부터 시작하는 정수 인덱스를 사용
# > 각각의 레이블 지정
data = pd.Series([2, 4, 6, 8, 10], index=['a', 'b', 'c', 'd', 'e'])
print(data)

# DataFrame
# : 2차원 레이블이 지정된 데이터 구조
# : 서로 다른 데이터 타입(정수, 문자열, 부동 소수점 숫자 등)의 열 포함 가능
# : 주로 여러 개의 딕셔너리가 포함, 딕셔너리의 값이 배열로 구성된 형태
# : 테이블(표)의 구성과 동일하다

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [28, 34, 29, 32],
    'City': ['부산', '서울', '경기', '대전']
}
df = pd.DataFrame(data)
print(df)

# DataFrame에 자동 지정되는 인덱스 번호 변경
df = pd.DataFrame(data, index=['#1', '#2', '#3', '#4'])
print(df)

#! DataFrame 데이터 접근
print('---데이터프레임의 데이터 접근---')

# 단일 열 선택
print(df['Name'])
# 여러 열 선택
# 대괄호 중첩 시: 이중 배열 - 2차원 배열
print(df[['Name', 'City']])

# 행 필터링
# : 조건에 따른 행의 데이터를 가져오기
result = df[df['Age'] >= 30]
print(result)

#! 데이터 조작
# 새로운 열을 추가
# : 새로운 열 추가 시 해당 데이터는
print(df)
df['Job'] = ['Developr', 'Employee', 'Doctor', 'Singer']
print(df)