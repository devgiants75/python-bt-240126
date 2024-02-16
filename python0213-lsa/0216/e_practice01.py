### 예외 처리 예제 ###

# 1. 이름 길이를 체크하는 예외 처리
# : 사용자로부터 입력받은 이름이 2 ~ 4자 사이가 아니면
#   NameError 예외를 발생
#   이름은 2 ~ 4자 사이로 입력해주세요. 라는 예외 메시지 출력

class NameError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    name = input('이름을 입력해주세요.')
    if len(name) < 2 or len(name) > 4 :
        raise NameError('이름은 2 ~ 4자 사이로 입력해주세요.')
except NameError as e:
    print(e)
else:
    print(f'입력된 이름은 {name}입니다.')

### 사용자 정의 예외를 포함한 예제 - 계좌 관리 시스템 ###
# 요구사항 정리
# - 계좌의 잔액이 요청된 출금액보다 적을 때: BalanceError 예외를 발생
# - 사용자로부터 출금액을 입력받고, 출금 가능 여부를 판단하여 결과를 출력

#! '사용자 정의 예외' 정의
# : 계좌의 잔액이 부족할 때 발생
class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)

#! 계좌 관리 클래스 구현
class Account:
    def __init__(self, balance):
        self.balance = balance # 계좌 잔액 초기화 - 인스턴스 변수

    def withdraw(self, amount): # 출금
        if self.balance < amount:
            raise BalanceError('계좌의 잔액이 부족합니다.')
        self.balance -= amount
        return amount

try:
    account = Account(10000) # 초기 잔액이 10,000원인 계좌 생성
    withdraw_money = int(input('출금액을 입력하세요.'))
    amount_money = account.withdraw(withdraw_money)
    print(f'{amount_money}를 출금했습니다. 현재 잔액은 {account.balance}입니다.')
except BalanceError as e:
    print(e)
except ValueError:
    print('유효한 금액을 입력하세요.')

### 사용자 정의 예외 - 비밀번호 검증 시스템 ###
# 요구사항
# - 비밀번호가 해당 조건을 만족하지 않을 경우 예외 발생
#   : 최소 8자 이상, 최소 하나의 숫자를 포함
# - 사용자로부터 비밀번호를 입력받고, 조건을 만족하는지 검증

#! 사용자 정의 예외
class PasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)

#! 비밀번호 검증 구현 함수
def validate_password(password):
    # char.isdigit() 함수는 문자가 숫자인지 판별
    # any() 함수는 주어진 시퀀스 중 어느 하나라도 참이면 True를 반환
    # : 모든 문자가 숫자가 아님을 의미
    # : 즉, 비밀번호에 숫자가 하나도 포함되지 않음을 의미
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise PasswordError('비밀번호는 최소 8자 이상, 최소 하나의 숫자를 포함')

try:
    pwd = input('비밀번호를 입력해주세요: ')
    validate_password(pwd)
    print('비밀번호가 성공적으로 설정되었습니다.')
except PasswordError as e:
    print(e)


