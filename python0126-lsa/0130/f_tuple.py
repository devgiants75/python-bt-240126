# Tuple 자료형
# : 리스트와 유사, 차이점(내부 값의 변경이 불가!)
# 순서O, 변경X, 중복O
# 소괄호()를 사용하여 생성, 각 요소는 쉼표(,)로 구분

# 1. Tuple 생성
tuple1 = () # 빈 튜플
tuple2 = (1, 2, 3) # 정수형 튜플
tuple3 = ('a', 'b', 'c') # 문자형 튜플
tuple4 = (1, 'a', 2.0) # 다양한 자료형의 혼합
tuple5 = (1, 2, (3, 4)) # 튜플 안에 튜플 (중첩 튜플)

# 2. 단일 요소(1개의 값)를 가지는 튜플 생성 시
#    , 요소 뒤에 쉼표를 반드시 붙여야 한다!
single_element_tuple = (1, )

# 3. Tuple 연산
# Tuple 덧셈, 곱셈
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2) # (1, 2, 3, 4, 5, 6)
print(tuple1 * 2) # (1, 2, 3, 1, 2, 3)
print(tuple1) # (1, 2, 3)

# 4. Tuple의 활용
# 요소의 위치를 반환하는 기능: index()
tuple = (1, 2, 3, 4)
print(tuple.index(3)) # 2 (요소 3의 인덱스 번호)
# 주어진 값과 일치하는 요소의 개수를 반환하는 기능: count()
tuple = (1, 2, 2, 3, 2, 3, 1, 2, 3)
print(tuple.count(2)) # 4

# 튜플은 요소값을 변경할 수 없기 때문에
# , 값을 변경하는 내장함수(기능)이 없다.