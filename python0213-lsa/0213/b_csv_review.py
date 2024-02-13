# 파이썬 CSV 파일 다루기 복습 예제 #
import csv

# 초기 데이터
data = [
    ['Name', 'Age', 'City'],
    ['이승아', '29', '부산'],
    ['이도경', '30', '부산'],
    ['김인택', '31', '대전'],
]

# b_csv_review.csv 파일 생성
filename = 'b_csv_review.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'{filename} 파일이 생성되었습니다.')

with open(filename, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))

# 특정 조건을 만족하는 데이터 필터링
# 예) 나이가 30 이상인 사람 찾기
print('===특정 조건 출력===')
with open(filename, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) # 한 줄 건너뛰기 - 헤더
    for row in reader:
        if int(row[1]) >= 30:
            print(','.join(row))


