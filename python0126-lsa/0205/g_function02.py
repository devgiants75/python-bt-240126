# 사칙 연산을 수행하는 함수 작성

# - 모든 함수에 return 사용

# add 함수: 두 수를 더하는 함수
def add(a, b):
    result = a + b
    return result
# subtract 함수: 두 수를 빼는 함수
def subtract(a, b):
    return a - b
# multiply 함수: 두 수를 곱하는 함수
def multiply(a, b):
    return a * b
# divide 함수: 두 수를 나누는 함수'
# >> 조건문을 사용하여 두 번째 인수가 0일 경우 '오류' 메시지를 출력
# >> 0이 아닐 경우에만 나누기 기능을 사용
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b

# 4개의 함수 호출
print(add(10, 5)) # 15
print(subtract(10, 5)) # 5
print(multiply(10, 5)) # 50
print(divide(10, 5)) # 2.0
# print(divide(10, 0)) - ZeroDivisionError: division by zero
print(divide(10, 0)) # Error: Cannot divide by zero!