# 컬렉션 타입

# list(리스트): 순서O, 변경 O, 중복O
# tuple(튜플): 순서O, 변경X, 중복O
# set: 순서X, 변경O, 중복X
# dictionary: 순서-,변경O, 중복(키X, 값O)

#! 딕셔너리를 사용한 항목 관리

# items변수에 사과, 바나나, 체리의
# , 항목을 키로 설정, 가격을 값으로 설정
items = {"사과": 2000, "바나나": 1500, "체리": 900}

# 사용자에게 물품 이름을 입력 받기
item_name = input('가격을 알고 싶은 물품 이름을 입력하세요.')

# 물품이 딕셔너리에 있는지 확인하고 가격을 출력
# 물품이 있으면 > 물품의 이름과 가격을 출력
    # {item_name}의 가격: {items[item_name]}
# 물품이 없으면 > 해당 물품이 없습니다 출력

if item_name in items:
    print(f'{item_name}의 가격: {items[item_name]}')
else:
    print('해당 물품이 없습니다.')

# 최소값과 최대값 판별
# 사용자로부터 세 개의 숫자 입력받기
num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))
num3 = int(input('세 번째 숫자: '))

# 최대값, 최소값 변수를 초기화
min_num = num1
max_num = num2

# 최소값 찾기
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3

print(f'최소값: {min_num}')

# 최대값 찾기
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

print(f'최대값: {max_num}')