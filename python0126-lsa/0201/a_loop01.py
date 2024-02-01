# 파이썬 제어문 - 반복문(Loop)

# 1. 반복문 정의
# : 특정 코드를 여러 번 실행하도록 프로그램에게 지시하는 구조

# 2. 반복문 종류
# : for반복문, while반복문

#! for 반복문
# : 시퀀스(리스트, 튜플, 문자열 등)를 순회하여 각 요소에 대해
#   , 특정 코드를 반복하도록 구현

# for 반복문의 기본 구조
'''
for 변수 in 시퀀스:
    반복할 명령 (실행할 코드 블럭)
'''

# for 반복문 예제
fruits = ['apple', 'mango', 'orange']

for fruit in fruits:
    print(fruit)

# 특정 횟수만큼 반복
# : range()함수
# : 연속된 숫자(정수)를 만들어주는 파이썬 내장 기능

# - range(n): 0부터 n-1까지 정수를 생성
# - range(n, m): n부터 m-1까지 정수를 생성
# - range(n, m, o): n부터 m-1까지 정수를 생성 (o는 숫자의 간격)

for i in range(5):
    print(i)

for i in range(1, 4):
    print(i)

for i in range(1, 10, 2):
    print(i)

#! 리스트, 튜플, 딕셔너리와 For문
numbers = [1, 2, 3, 1, 5]
for number in numbers:
    print(number)

languages = ('Python', 'Java', 'C++')
for language in languages:
    print(language)

fruitColors = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
for fruit, color in fruitColors.items():
    print(f'The color of {fruit} is {color}')

# .items(): 딕셔너리의 모든 키-값 쌍을 반환하는 메서드
# 키: keys()
# 값: values()