# 파이썬 데이터 타입 (기본 데이터 타입)

# 1. 숫자형: 숫자(Number) 형태로 이루어진 자료형
# : 정수(int)와 실수(float)

# 정수 (int)
# : 양의 정수, 0, 음의 정수를 포함하는 데이터
# 5, -3, 0 등
int_number = 1 # 줄 복사: ctrl + d
int_number = -3
int_number = 0 # 파이썬은 하나의 변수에 재할당이 가능

# >> int() 함수: 다른 데이터 타입을 정수형으로 변환하는 기능
int_number = int(3.5)
print(int_number)
print(int("7"))

# 실수 (float)
# : 소수점이 있는 숫자
# 3.14, -0.01, 2.0 등
float_number = 3.14
float_number = -0.01
float_number = 2.0

# >> float() 함수: 다른 데이터를 실수형으로 변환
print(float(3))
print(float("7"))

# 2. 논리형(boolean: 불리언)
# : 참(True)과 거짓(False)의 두 개의 값만을 나타내는 자료형
# : 반드시 첫문자를 대문자로 사용
bool_data = True
bool_data = False
    # bool_data = true - Error
# >> bool() 함수: 다른 데이터 타입을 bool 타입으로 변환
# : 각 데이터 별 비워진 값은 False ( 0, '', None, [], {}, () )
# : 그 외의 값은 True로 간주
print(bool(0)) # False
print(bool('')) # False
print(bool(None)) # False - None: 아무것도 없다.

print(bool(123)) # True
print(bool('안녕하세요')) # True

# 3. 문자열(str, string)
# : 문자, 단어 등으로 구성된 문자들의 집합
# : 작은따옴표(')나 큰따옴표(")로 쌍으로 묶어 표현
str_data = "hello"
str_data = 'python' # shift + tab: 역방향 탭
# >> str() 함수: 다른 데이터 타입을 문자열로 변환
print(str(100)) # 문자열 "100"
print(str(True)) # 문자열 'True'