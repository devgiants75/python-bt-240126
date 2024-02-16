### 파이썬 예외 처리 ###

# 1. 강제로 예외 발생시키기
# : 파이썬에서는 raise 키워드를 사용해 강제로 예외 발생
# : 특정 조건에서 예외를 발생시켜 의도적으로 프로그램을 중단하거나
# : , 예외를 처리하고 싶을 때 사용

# raise문 사용법
# : raise 예외클래스()
# : raise 예외클래스('예외 메시지')

age = int(input('나이를 입력하세요: '))

if age < 0:
    # 예외 처리가 아닌 예외 발생
    raise ValueError('나이는 음수일 수 없습니다.')
else:
    print(age)

# 2. 사용자 예외 클래스 정의
# 파이썬에서 내장 예외 클래스 외에 사용자가 직접 예외 클래스를 정의

# 사용자 예외 클래스의 기본 형태
# class 예외클래스명(부모클래스):
#   def __init__(self):
#       super().__init__('예외메시지')

class HourError(Exception):
    def __init__(self):
        super().__init__('올바른 시간이 아닙니다.')

try:
    hour = int(input('시간을 입력하세요: '))
    if hour < 0 or hour > 23:
        raise HourError
except HourError as message:
    print(message)