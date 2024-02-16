### 예외 처리 ###

# 1. if 조건문 (고전적인 예외 처리 방법)
# 사용자로부터 두 개의 정수를 입력받아 나눗셈을 구현

# - 예제
# a = int(input('정수를 입력하세요.'))
# b = int(input('정수를 입력하세요.'))

# result = a / b - ZeroDivisionError: division by zero
# print(result)

# - 예제
# if b == 0:
#     print('0으로 나눌 수 없습니다!')
# else:
#     result = a / b
#     print(result)

### 파이썬 예외의 종류 (파이썬의 내장 예외) ###

# 1. BaseException
# : 최상위 예외 클래스 (파이썬의 내장 예외는 반드시 해당 클래스를 상속)
# : 주로 직접 X, 해당 클래스를 상속받는 자식 클래스를 사용

# 2. ValueError
# : 잘못된 값이 입력될 때 발생
# ex. 정수가 예상되는 곳에 문자열이 전달

# 3. TypeError
# : 잘못된 타입의 데이터 연산 시 발생
# ex. 숫자 대신 문자열을 더하려고 할 때

# 4. ZeroDivisionError
# : 0으로 나누려고 할 때 발생

# 5. SyntaxError
# : 프로그램의 문법이 잘못되었을 경우 발생
# ex. 들여쓰기, 괄호의 불일치, 오타 등

### 파이썬 예외 처리 방식 ###

# 1. 모든 예외를 처리하는 방식
# : 예외의 종류와 상관없이 모든 예외를 잡아서 처리
# : 가능한 특정 예외를 지정하여서 처리하는 것을 권장
# try - except 문을 사용하여 예외 처리

# 모든 예외 처리의 기본 형태
# try:
#   코드 작성 영역
# except:
#   예외 발생 시 처리 영역

# - 예제
# try:
#     a = int(input('정수를 입력하세요: '))
#     b = int(input('정수를 입력하세요: '))
#     print('{} / {} = {}'.format(a, b, a / b))
# except:
#     print('예외가 발생하였습니다.')

# 2. 특정 예외만 처리하는 방식
# : except 절은 여러 개를 동시에 사용 가능
# : except 절 뒤에 처리할 예외명을 생략하면 예외의 종류와 상관없이 처리

try:
    a = int(input('정수를 입력하세요: '))
    b = int(input('정수를 입력하세요: '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:
    # Exception 예외의 경우
    # : 그 외의 모든 예외를 처리하는 코드 (예상치 못한 문제를 처리)
    print('기타 오류가 발생하였습니다.')

# 3. 예외 메시지를 처리
# : 모든 예외는 기본적으로 예외 메시지를 내장
# : as 키워드를 통해 except문의 예외 메시지를 가져올 수 있다.

# 예외 메시지 처리의 기본 형태
# try:
#   코드 작성 영역
# except 예외명 as 예외메시지명:
#   예외 발생 처리 영역 - 예외 메시지명으로 출력

# 리스트에 존재하지 않는 인덱스번호를 사용할 경우: IndexError 예외 발생

arrays = [10, 20, 30, 40, 50]

# print(arrays[10]) - IndexError

try:
    arrays[10]
except IndexError as message:
    print(message) # list index out of range

try:
    a = int(input('정수 입력: '))
    b = int(input('정수 입력: '))
    print(f'{a / b}')
except ZeroDivisionError as e1:
    print(e1) # division by zero
except ValueError as e2:
    print(e2) # invalid literal for int() with base 10: 'dfhjj'