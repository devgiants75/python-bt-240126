# 연산자 예제

# 1. 임의의 두 자리 정수(10 ~ 99)를 입력받아서
# 십의 자리와 일의 자리로 분리하여 출력하는 프로그램을 구현

number = int(input('두 자리 정수를 입력해주세요(10 ~ 99) : '))
tens = number // 10
ones = number % 10
print((tens * 10) + ones)