### 파이썬의 외부 라이브러리를 활용한 엑셀 파일 활용 ###
import pandas as pd

#! 1. 엑셀 파일 불러오기
# pandas의 read_excel('파일경로') 함수를 사용하여
# , 엑셀 파일을 DataFrame의 형태로 불러오기

# 파일 경로 지정
file_path = 'aa.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(file_path)
print(df)

# 데이터 조회하기
# 1. 상위 데이터 조회
# : head()함수 사용 시 데이터 프레임의 상위 5개 행을 조회
print(df.head())

# 2. 데이터 프레임의 정보 조회
# : info() 메서드를 사용하여
# : , 데이터프레임의 구조(컬럼), 각 컬럼의 데이터 타입 등의 정보 조회
df.info()

# 3. 기초 통계 정보 조회
# : describe() 메서드 사용
# : , 수치형 컬럼들에 대한(숫자형) 기본 통계 정보
# : , 평균, 표준편차, 최소값, 최대값 등을 조회
print(df.describe())

### pandas를 사용한 엑셀 불러오기 실습 ###
# 1. 엑셀 파일 경로 지정
file_path = 'aaa.xlsx'

# 2. pandas 라이브러리의 read_excel함수 사용하여
#    DataFrame 형태로 불러오기
df = pd.read_excel(file_path)

# 3. 상위 5개의 행을 출력하여 조회
print('상위 5개 행 조회')
print(df.head())

# 4. 해당 DataFrame의 정보를 조회
print('---데이터프레임 정보---')
df.info()

# 5. 수치형 데이터에 대한 기초 통계 정보를 조회
print('---기초 통계 정보---')
print(df.describe())