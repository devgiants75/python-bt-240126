# if, for문 복습 문제 #

# 사용자로부터 차량번호를 입력받아, 차량번호가 짝수로 끝나면 '운행가능'
# , 아닐 경우에는 '운행불가'를 출력하는 프로그램

# 사용자로부터 차량 번호를 입력받기
car_number = input('차량 번호를 입력해주세요')

# 입력받은 차량 번호에서 마지막 숫자를 추출
last_digit = int(car_number[-1])

# 마지막 숫자가 짝수인지 홀수인지 판별
if last_digit % 2 == 0:
    print('운행 가능')
else:
    print('운행 불가')

# if문 복습 예제 2
# 영화 평점을 입력받아, 해당 평점에 따라 다른 메시지를 출력

# 평점이 4.0 이상이면 'Excellent'
# 평점이 2.0 ~ 3.9 사이면 'SoSo'
# 평점이 1.9 이하면 'Bad'

# 형 변환
# int(): 정수로 변환
# float(): 실수로 변환

ratingInput = input('영화 평점을 입력해주세요.')
rating = float(ratingInput)

if rating >= 4.0:
    print('Excellent')
# elif rating >= 2.0 and rating < 4.0:
elif 2.0 <= rating < 4.0:
    print('SoSo')
elif rating <= 1.9:
    print('Bad')
else:
    print('올바른 평점 범위를 입력해주세요.')