# 파이썬 제어문 - 반복문

#! while문

# 1. while문 정의
# : 주어진 조건이 참(True)인 동안 실행할 명령을 반복
# : >> 조건이 거짓이 될 때까지

# 2. while문 기본 구조
'''
while 조건:
    실행할 코드(조건이 참인 동안에)
'''

# 조건식에는 루프(반복)가 계속 실행되는지 아니면 중단될지를 결정하는
# , boolean타입 표현식

# 변수를 1씩 증가 시켜서 5보다 작을 때까지 출력
count = 0
while count < 5:
    print(count)
    count += 1 # count = count + 1

# while True:
#     print('무한루프')

# 파이썬의 무한루프를 빠져나오는 단축키: ctrl + f2

# break
# : 반복문을 즉시 종료 (무한루프 종료)

# 정수를 0 부터 9까지 range()함수로 나열할 때 (10번 반복)
# , 해당 정수가 5가되면 종료
for i in range(10):
    if i == 5:
        break
    print(i)

while True:
    userInput = input('종료하려면 q를 입력하세요: ')
    if userInput == 'q':
        break

# continue
# : 현재 반복을 건너뛰고 다음 반복으로 넘어감
# : 루프의 현재 반복의 나머지를 중지, while문의 조건을 다시 확인

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 사용자로부터 숫자만 입력받도록 구현
# isdigit(): 문자열이 숫자로만 이루어져있는지 확인하는 함수
# >> 문자가 단 하나라도 있으면 False
# >> 모든 문자가 숫자로만 이루어져있으면 True를 반환

while True:
    userInput = input('종료하려면 q를 입력하세요')
    if userInput == 'q':
        break
    # 문자가 존재하는 경우 False이기 때문에 if문 안의 실행을 위해서
    # , not 연산을 사용
    if not userInput.isdigit():
        print('숫자만 입력해주세요')
        continue
    print(f'입력하신 숫자는 {userInput}입니다.')