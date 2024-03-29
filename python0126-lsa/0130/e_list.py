# 파이썬의 컬렉션(collection) 타입
# : 다양한 데이터를 그룹화하여 관리할 수 있는 자료형

#! 파이썬 컬렉션 타입 종류
# List: 순서O / 변경O / 중복O
# Tuple: 순서O / 변경X / 중복O
# Set: 순서X / 변경O / 중복X
# Dictionary: 키-값 쌍으로 저장 / 변경O / 키(중복X), 값(중복O)

# List 자료형
# : 여러 값을 순서대로 저장할 수 있는 컬렉션 타입
# : 대괄호[]를 사용하여 생성, 각 요소는 쉼표(,)로 구분
# (요소: 컬렉션 내의 각 데이터)

# 1. 리스트 생성
# 리스트명 = [요소1, 요소2, 요소3, ...]
list1 = [] # 빈 리스트
list2 = [1, 2, 3] # 정수형 리스트
list3 = ['a', 'b', 'c'] # 문자형 리스트
list4 = [1, 'a', True] # 다양한 자료형의 혼합
list5 = [1, 2, [3, 4]] # 리스트 안에 리스트 (중첩 리스트)

# 리스트 인덱싱 & 슬라이싱
# list 인덱싱
# : 리스트명[인덱스번호]
list = [1, 2, 3, 4, 5]
print(list[0]) # 1
print(list[3]) # 4
print(list[-2]) # 4

# 리스트 슬라이싱
# : 리스트명[시작번호:끝번호]
# : 시작번호는 포함O, 끝번호는 포함X
print(list[1: 4]) # [2, 3, 4]

#! 리스트의 활용
# 1. 리스트의 연산(+, *)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2) # [1, 2, 3, 4, 5, 6]
print(list1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 2. 리스트의 길이
# : len()
# : 요소의 개수
print(len(list1)) # 3

# 3. 리스트 추가, 수정, 삭제
list = [1, 2, 3]

# append(): 요소 추가
list.append(4) # 제일 마지막 위치에 요소를 추가
print(list) # [1, 2, 3, 4]

# del: 요소 삭제
# del 리스트명[인덱스번호]
del list[0]
print(list) # [2, 3, 4]

# 인덱스 번호를 사용하여 요소 수정
# 리스트명[인덱스번호] = 데이터
list[2] = 10
print(list) # [2, 3, 10]