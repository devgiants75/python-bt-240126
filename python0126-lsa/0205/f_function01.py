# 파이썬 함수 #

#! 함수
# : 하나의 특정한 목적의 작업을 수행하기 위해
#   독립적으로 구성된 프로그램 코드의 집합
# : 특정한 값 x를 인수로 전달받으면, 반드시 특정 값 y를 결과로 반환

#! 함수의 구성
# 함수 정의: 함수를 새로 생성
# 인수(인자): 함수에 전달할 입력(input) - argument
# 매개변수: 인수를 받아서 저장하는 변수 - parameter
# 반환값: 함수의 출력(output) - return
# 함수 호출: 만들어진 함수를 실제로 사용하는 것

#! 함수의 정의
# : def 키워드를 사용하여 함수를 정의 (definition)
# : 함수 이름과 괄호 안에 파라미터를 명시
# : 함수 본문은 콜론(:) 다음 들여쓰기 하여 작성

#! 함수의 기본 형태
# : 매개변수와 반환값은 선택

# def 함수명(매개변수):
#     실행할코드
#     return 반환값

def greet():
    print('안녕하세요 만나서 반갑습니다 :)')

#! 함수 호출
# : 함수명 다음에 ()괄호를 붙여서 호출
# : 매개변수값이 존재하는 경우 사용할 인수를 소괄호 안에서 작성
greet()
greet()
greet()

#! 파라미터와 인수 - 선택 (필수X)
# 1. 인수 X
greet()

# 2. 인수 O (한 개)
def arg(number):
    print(f'인수가 {number} 개 입니다.')

# arg(1, 3) - Error
# : 지정된 매개변수의 수와 전달하는 인수의 개수가 같아야 한다.

# 3. 인수 O (여러 개)
# : 파라미터와 인수를 ,(콤마)로 구분하여 나열

# - 위치 인수를 사용
# : 콤마로 구분된 매개변수의 순서대로 값을 전달

# - 기본값 인수
# : 매개변수 내에서 해당 값을 지정
# : 함수 호출 시 데이터 전달을 하지 않을 경우 기본값 사용
# : 데이터 전달을 하는 경우 재할당되어 전달값 사용
def arguments(name, age, city='부산'):
    print(f'이름은 {name}, 나이는 {age}, 도시는 {city}입니다.')

arguments('이승아', 28)
arguments(28, '이승아')

# - 키워드 인수를 사용하여 호출
arguments(age=28, name='이승아')

# - 기본값 인수 사용
# arguments() - Error

# : 기본값을 지정하지 않은 인수를 함수 호출 시 전달하지 않을 경우
# : >> 오류

# : 기본값 지정 인수도 함수 호출 시 재할당이 가능
# >> 위치 인수, 키워드 인수 모두 사용 가능
arguments('이승아', 28, '대전')

# 함수 명명 규칙
# : lower_snake_case 사용
# 덧셈 기능의 함수: sum_input

#! 함수의 반환값 - 선택 (필수X)
# : return 키워드를 사용하여 함수의 결과값을 반환
# : 함수에서는 return을 만나면 함수 실행이 종료, 값을 반환

# 두 숫자를 더한 결과를 반환하는 함수
def add(a, b):
    result = a + b
    return result

# 반환값 사용 시 (ex. 출력)
# : 변수에 담아 사용
result = add(1, 2)
print(result) # 3

#! 여러 값 반환(다중 반환)
# : 하나의 return문을 사용하여 여러 값을 반환
# : 튜플 형태로 반환
def min_max(numbers):
    # 파이썬의 컬렉션 타입의 내장 함수
    # : 최소값과 최대값을 반환
    min_result = min(numbers)
    max_result = max(numbers)
    return min_result, max_result

array = [1, 2, 3, 4, 5]
number = min_max(array)
print(number) # (1, 5)

# 조건문에 따른 다른 값 반환
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(5)) # False
print(is_even(6)) # True

# return이 없는 함수
# : 호출이 완료되면 None(아무것도 없음)을 반환
# : 보통 함수 호출 시 곧바로 출력을 사용할 때 작성
def none_return(name):
    print(f'Hello, {name}')

result = none_return('이승아')
print(result) # None