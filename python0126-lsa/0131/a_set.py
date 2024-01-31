# 파이썬 컬렉션 타입 - set

# set
# : 여러 아이템을 순서X, 변경O, 중복X

# set 자료형 생성
# 1. {} 중괄호를 사용하여 생성, 각 요소는 쉼표(,)로 구분
# 2. set() 함수를 사용하여 생성

set1 = {1, 2, 3} # 중괄호를 사용한 세트 생성
set2 = ([1, 2, 3, 2]) # 리스트를 사용한 세트 생성
# {1, 2, 3}
set3 = set() # 빈 세트 생성
set4 = set('Hello') # 문자열을 이용한 세트 생성
# {'H', 'e', 'l', 'o'}

# set은 순서가 없기 때문에
# , 인덱싱과 슬라이싱 등의 연산 지원 X

# set의 활용
# 1. set에 요소 추가 & 제거
# 요소 추가: set명.add(추가값)
my_set = {1, 2, 3}
my_set.add(4)
# my_set.add(2) - set은 중복 불가! (오류X)
print(my_set)

# 여러 개 요소 추가: update(추가데이터들)
my_set.update([4, 5, 6, 7])
print(my_set)

# 주어진 값이 있는 항목을 제거
# set명.remove(값)
my_set.remove(2)
# my_set.remove(8) - Error (존재하지 않는 값 삭제 시 에러 발생)
print(my_set)

# set명.discard(값)
my_set.discard(8) # 존재하지 않는 값을 삭제해도 에러 발생 X
print(my_set)

# set의 연산
# : 수학적 집합 연산이 가능
# 1. 합집합(union): |(vertical bar), union()
# 2. 교집합(intersection): &(앰퍼샌드), intersection()
# 3. 차집합(difference): -(하이픈), difference()
a = {1, 2, 3}
b = {3, 4, 5}

union_set = a | b # 합집합
print(union_set) # {1, 2, 3, 4, 5}

intersection_set = a & b # 교집합
print(intersection_set) # {3}

difference_set = a - b # 차집합
print(difference_set) # {1, 2}