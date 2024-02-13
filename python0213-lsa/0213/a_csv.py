# CSV 파일 입출력 #

# CSV 파일
# : CSV(Comma Separated Values) 파일
# : 쉼표로 분리된 값
# : 필드(데이터)를 쉼표로 구분한 파일, 표 형태의 데이터 저장에 활용
# - 열: 쉼표로 구분
# - 행: 새 줄로 구분

'''
이름, 학년, 반
이승아, 1학년, 3반
이도경, 3학년, 7반
'''

#! 1. CSV 파일 읽기
# : 한 줄에 한 데이터 읽기: readline() 메서드로 한 줄씩 읽기
#   - 행의 데이터
# : 쉼표로 분리: split() 메서드로 분리
#   - 열의 데이터

# 빈 리스트: 학생 정보를 저장할 리스트
student_list = []

# open() 함수를 사용하여 csv 파일을 열기
# 첫 번째 줄(헤더)를 읽기
# 파일을 끝까지 반복하여 한 줄씩 읽기
# 더 이상 읽을 줄이 X 반복 종료
# 읽은 데이터를 쉼표로 분리하여 리스트에 저장
# 분리된 데이터를 student_list에 추가
# 파일로부터 읽은 데이터 출력
with open('a_student.csv', 'rt', encoding='utf-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)

print(student_list)

#! 2. csv 모듈을 사용한 파일 읽기
# csv 모듈의 reader() 메서드 사용
# : csv 파일의 내용을 읽고, 그 내용을 저장한 객체를 반환

import csv

print('===csv 모듈 사용===')
with open('a_student.csv', 'rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    # reader 객체를 순회하여, 파일의 각 줄을 출력
    for row in reader:
        print(row)

#! 3. csv 모듈로 CSV 파일 생성
# csv.writer 객체를 이용하여 csv 파일 작성 가능
# : csv 파일에는 문자열의 데이터만 작성 가능
header = ['name', 'age', 'gender']
data = [
    ["이승아", "28", "여"],
    ['김인택', '29', '남'],
    ['이도경', '30', '여']
]

with open('person.csv', 'wt', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # 한 줄 추가: writerow
    # 여러 줄 추가: writerows
    writer.writerow(header)
    writer.writerows(data)

print('csv 파일이 생성되었습니다.')