# c_inner_func03

# 파이썬 내장 함수

# 3. 시퀀스 자료형: 요소들이 연속적으로 이어진 자료형
# ex) 리스트, 튜플, 문자열 등

# - enumerate()
# : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태로 반환

# for item in enumerate([리스트]):
    # 반복 실행문
for item in enumerate(['가위', '바위', '보']):
    print(item)
# (0, '가위')
# (1, '바위')
# (2, '보')

# - range(): 숫자 리스트를 생성하는데 사용
#           , 주로 for문에서 사용 (일정한 간격의 숫자 시퀀스 생성)

# range(stop): 0부터 stop-1까지의 정수를 반환
for i in range(5):
    print(i) # 0 ~ 4

# range(start, stop): start부터 stop-1까지의 정수를 반환
for i in range(1, 5):
    print(i) # 1 ~ 4

# range(start, stop, step): start부터 stop-1까지 step간격으로 반환
for i in range(0, 10, 2):
    print(i)

# - len(s): s의 원소 개수를 반환
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # 5
my_string = "Hello, Python!"
print(len(my_string)) # 14

# - sorted()함수
# : 리스트를 정렬하여 반환 (기본-오름차순 정렬)
# : 내림차순 정렬: reverse=True

my_list = [5, 1, 3, 2, 4]
print(sorted(my_list)) # [1, 2, 3, 4, 5]
print(sorted(my_list, reverse=True)) # [5, 4, 3, 2, 1]

# - zip() 함수
# : 여러 개의 순회 가능한 값을 받아
# : 각 객체의 동일한 인덱스에 있는 요소들끼리 짝지어 튜플로 반환

list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

result = zip(list1, list2)

for i in result:
    print(i)
# (1, 'one')
# (2, 'two')
# (3, 'three')

# 각각의 순회 가능한 값의 길이가 다를 경우
# : 동일한 인덱스 번호의 값만 추출 (가장 짧은 길이의 값을 기준으로 반환)

list1 = [1, 2, 3]
list2 = ['one', 'two']

result = zip(list1, list2)
for i in result:
    print(i)
# (1, 'one')
# (2, 'two')