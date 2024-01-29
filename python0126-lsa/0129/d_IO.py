#! 파이썬의 기본 입출력

# 1. 출력
# 기본 출력: print() 함수
print("파이썬의 기본 출력")

# 이스케이프 문자: 문자열 내에서 특수한 의미를 가지는 문자 조합
# \(백슬리시)로 시작, 특정 문자와 함께 사용
# \n : 줄바꿈
# \\ : 백슬래시(\) 문자 그 자체
# \' \" : 따옴표 문자 그 자체
print("Hello\nWorld")
print("경로를 표시 https:\\\\naver.com")
# 서로 다른 따옴표 안의 사용은 인식 가능
# , (큰) 따옴표 안의 (큰) 따옴표 사용은 인식 불가
print("그가 말했다. \"안녕\"")

# print()함수에 여러 개의 데이터를 출력
# : 콤마(,)로 구분하여 나열
# sep: 출력할 여러 값들 사이에 들어갈 문자를 지정, 기본값(공백)
print("Apple", "Banana", "Orange", sep=", ")

#! 포맷팅을 사용한 출력
# : 문자열 내에 변수나 값의 내용을 삽입하는 방법

# 1. %연산자 포맷팅
# : 문자열 내에 % 기호 뒤 특정 포맷 코드를 사용해 해당 위치에
# : , 변수나 값을 삽입

# 기본 포맷 코드
# %s: 문자열(모든 데이터 가능), %d: 정수, %f: 부동소수점 숫자
# >> %f의 경우 사용하고자 하는 소수점 자리수를 명시
# : %.2f (소수점 두 번째 자리까지)
# %%: %기호 문자 그대로를 사용

print('Hello, %s' %'python')
print('이름: %s, 나이: %d, 키: %.1fcm' %("이승아", 30, 169.23))
# 포맷 코드의 경우 여러 가지 포맷 코드를 사용하여
# , 여러 데이터 타입을 출력 가능
# 많이 사용되지 않는 방법
# (Python 3.6 버전 이상에서는 f-string 사용을 권장)

# 2. format() 함수 사용
# : 문자열 내의 중괄호 {} 자리 값에 값을 삽입하는 방법
welcome_message = "Hello, {}!".format("LSA")
print(welcome_message)
print('{} {} {} {}'.format("I", "have", 4, "apples"))

# 3. f-string 포매팅
# : Python 3.6 버전 이상에서
# : , 사용할 수 있는 현대적인 문자열 포맷팅 형식
# : 중괄호 내에 직접 변수나 표현식을 넣어 쉽게 데이터 삽입 가능
# : 표현식 지원(문자열 내에서 변수, +, - 등의 연산식 사용 가능)
name = "이승아"
height = 169.2
print(f'My name is {name} and I am {height}cm tall')

a = 5
b = 3
print(f'Five times three is {a * b}')

number = 7
print(f'다음 숫자는 {number + 1}입니다.')

# f-strings에서는 중괄호 내에 콜론(:)을 사용하여 포맷 지정
# : 소수점 자리를 포맷
number = 3.14159
print(f'소수점 두 자리: {number:.2f}')

# 2. 입력
# input() 함수를 사용하여 사용자로부터 입력을 받음.
# input() 함수를 실행하는 경우 프로그램은 사용자의 입력을
# , 문자열로 인식하여 읽어들임.

# 사용방법
# input의 소괄호 내에 따옴표로 입력에 대한 메시지를 출력
# input('이름을 입력해주세요.')
user_input = input('이름을 입력해주세요.')
# 영문자가 아닌 한글을 입력하는 경우 인식이 느림
print(user_input)

user_input = input('키를 입력해주세요') # "169.2
# int(), float() 등을 사용하여 해당 데이터로 변환
height = float(user_input)
print(height)

# 사용자로부터 두 개의 실수를 입력받아
# , 그 합계를 계산하는 프로그램 구현

# 첫 번재 실수 입력받기
number1 = float(input('첫 번째 실수를 입력하세요: '))
# 두 번째 실수 입력받기
number2 = float(input('두 번째 실수를 입력하세요: '))

# 두 실수 합계 계산
sum = number1 + number2

# 결과 출력 f-strings을 사용하여 출력
print(f'두 실수 의 함계는 {sum}입니다.') # 5.7

# 거스름돈 계산: 금액은 정수로 표현
# 사용자로부터 구매 금액 입력 purchase_amount
# 사용자로부터 지불 금액 입력 payment_amount

# 거스름돈을 계산 (구매 금액 - 지불 금액) change