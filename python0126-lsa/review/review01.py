# 1. 변수 할당과 출력
# 문제: 파이썬에서 변수 x에 숫자 10을 할당하고
# , x의 값을 출력하는 코드를 작성
x = 10
print(x)

# 2. 다음 중 파이썬에서 유효하지 않은 변수 이름 선택
# A) my_var
# B) 2nd_var - 파이썬 변수명은 숫자로 시작할 수 X
# C) var_name
# D) _myvar

# 3. 변수 값 교환
# 변수 a에 100을, 변수 b에 200을 할당한 뒤, 두 변수의 값을 교환
a = 100
b = 200
a, b = b, a # a, b = 200, 100

# 4. 데이터 타입 확인
# 변수 a = "Hello, World!"의 데이터 타입을 확인하는 코드를 작성
# type() 함수 사용
a = "Hello, World!"
print(type(a)) # <class 'str'> - 문자열 타입

# 5. 문자열 연결
# first_name과 last_name 두 변수 작성
# , 위 두 변수를 공백을 포함하여 연결하는 코드를 작성
# ex) first_name = "John" / last_name = "Doe"
# >>>>>  결과 "John Doe"
first_name = "John"
last_name = "Doe"
full_name = "John" + " " + last_name
print(full_name) # John Doe

# 6. 리스트 요소 추가
# 빈 리스트 my_list 생성
# ,리스트에 숫자 1, 2, 3을 차례대로 추가하는 코드를 작성
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list) # [1, 2, 3]

# 7. 딕셔너리 키-값 접근
# prices = {'apple': 2.99, 'banana': 1.99, 'orange': 1.49}
# , 'apple'의 가격을 출력하는 코드를 작성
prices = {'apple': 2.99, 'banana': 1.99, 'orange': 1.49}
# 값 접근: 딕셔너리명[키]
print(prices['apple']) # 2.99

# 8. 집합의 중복 제거
# 리스트 my_numbers = [1, 2, 2, 3, 4, 4, 4, 5]에서 중복을 제거하여
# , 모든 고유 숫자를 포함하는 집합을 생성하는 코드를 작성
my_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
set_numbers = set(my_numbers)
print(set_numbers) # {1, 2, 3, 4, 5}