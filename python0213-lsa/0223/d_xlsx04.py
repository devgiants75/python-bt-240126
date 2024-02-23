### pandas을 사용한 엑셀 파일 활용 ###

# openpyxl의 엑셀 불러오기 - 파일 그대로를 가져와서 저장
# pandas의 엑셀 불러오기 - DataFrame 형태로 변환
# : 각각의 데이터의 구조를 사용 가능 (파악하기 용이)

# 셀 내용 수정 및 삽입
import pandas as pd
df = pd.read_excel('aaaa.xlsx')

# 두 번째 행의 City 열 값을 변경
# loc 기능을 사용 (locate-위치)
# : 데이터 행부터 인덱스 번호 시작
df.loc[1, 'City'] = '대전'

# 셀 내용 삽입
df.loc[5] = ['추가윤', '양산', 30]

# 반복문을 사용하여 셀 정보에 접근
# : 모든 행의 'Name'열에 접근
for index, row in df.iterrows():
    print(row['Name'])

# 특정 열 추가
df['Age'] = [28, 27, 26, 28, 35, 29]

# 특정 열 삭제
# drop('삭제하고자하는 열의 이름')
# axis=1(열), axis=0(행)
# inplace=True
# (원본 데이터 수정, False인 경우 기존 프레임은 유지하고 새로운 데이터 프레임이 반환)
df.drop('Age', axis=1, inplace=True)

df.to_excel('aaaa.xlsx', index=False)