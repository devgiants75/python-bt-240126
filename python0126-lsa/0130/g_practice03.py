# 리스트 & 튜플 예제

# 문제 설명(로직)
# 식료품점에 구매할 물품과 각각의 가격
groceries = [("사과", 5000), ("우유", 3000), ("빵", 1500)]

# 각 항목의 가격을 계산
apple_price = groceries[0][1]
milk_price = groceries[1][1]
bread_price = groceries[2][1]

# 총 구매 금액을 계산
total_price = apple_price + milk_price + bread_price

# 결과 출력
print(total_price) # 9500

# 연산자 복습 문제
# BMI(체질량) 계산기 프로그램
# : 체중(kg)을 키(m)의 제곱으로 나눈 값

# 사용자로 부터 체중과 키를 입력받아 BMI를 계산하는 공식

weight = float(input("체중(kg)을 입력하세요: "))
height = float(input("키(m)를 입력하세요: "))

bmi = weight / (height ** 2)

# 결과 출력
print("계산된 BMI: ", bmi)

# 연산자 복습 문제 #
# 1분은 60초이고, 1시간은 60분입니다. 따라서 1시간은 3600초입니다.
# 임의의 초를 입력받아 해당 초를 시, 분, 초로 변환하여
# 출력하는 프로그램을 구현해주세요

# 입력받은 초를 담는 변수 total_seconds