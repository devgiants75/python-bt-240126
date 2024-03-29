# 파이썬의 제어문 - 조건문

# 제어문
# : 프로그램의 흐름을 제어하는 경우에 사용하는 실행문
# : 조건문, 반복문 등

#! 조건문
# : 특정 조건을 충족할 경우 특정 코드 블럭을 실행하는 구문

# if문: 만약 ~ 라면
# - 해당 조건이 참(True)인 경우에만 코드 블럭을 실행

# 기본구조
# if 조건:
#   (조건이 True인 경우)실행할 코드

# > 조건: 참(True) 또는 거짓(False)의 값을 갖는 표현식
# > 실행할 코드: if문 바로 아래에 들여쓰기 하여 작성

# 기본 if문
# : 어떤 수가 10보다 큰지 확인하는 조건문 작성
num = 9

if num > 10:
    print('The number is greater than 10')

# else문
# : 그밖에, 그렇지 않다면
# : if문의 조건이 충족되지 않을 때(즉, if의 조건이 False일 때)
# : , 실행되는 코드 블럭

# 기본 구조
'''
if 조건:
    조건이 True일 때 실행할 코드
else:
    조건이 False일 때 실행할 코드
'''

# 어떤 수가 10보다 큰지 확인,
# 10보다 클 경우 '성공', 10보다 작을 경우 '실패'

level = 11

if level > 10:
    print('성공')
else:
    print('실패') # level이 10 이하인 경우의 조건이 생략

# 중첩 if-else문
# : if나 else 블럭 내부에서 다른 if-else 구문 작성
'''
if 조건1:
    조건1이 참일 때 실행할 코드
    if 조건2:
        조건1과 조건2가 모두 참일 때 실행할 코드
    else:
        조건1은 참이지만, 조건2는 거짓일 때 실행할 코드        
else:
    조건1이 거짓일 때 실행할 코드
'''

# number 가 0보다 큰지 아닌지를 확인
# 0보다 클 경우에는 해당 number가 짝수인지 홀수인지를 확인

number = 12
if number > 0:
    print('양수입니다.')
    if number % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
else:
    print('양수가 아닙니다.')

# elif 문: else if의 줄임말
# - 여러 조건을 순차적으로 확인할 경우
# - if문과 else문 사이에 작성(개수의 제한 X)
'''
if 조건1:
    조건1이 참일 경우 실행할 코드
elif 조건2:
    조건1이 거짓이고, 조건2가 참일 때 실행할 코드
elif 조건3:
    조건1, 2가 거짓이고, 조건3이 참일 때 실행할 코드
else:
    모든 조건이 거짓일 때 실행할 코드
'''

# 나이에 따라 어린이, 청소년, 성인으로 구분
age = 12
if age <= 13:
    print('어린이입니다.')
elif age > 13 and age <= 19:
    print('청소년입니다.')
else:
    print('어른입니다.')

# 조건문과 삼항 연산자
# if-else문을 더 간결하게 표현하는 방법

# 기본 구조
# 참일 때의 값(코드) if 조건 else 거짓일 때의 값(코드)

# 어떤 수 num이 10보다 큰지 아닌지를 판단하여 문자열 출력
num = 5
result = '10보다 큽니다.' if num > 10 else '10보다 작습니다.'
print(result)






