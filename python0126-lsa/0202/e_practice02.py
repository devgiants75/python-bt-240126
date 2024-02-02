# 1. 가위 바위 보 게임

# random 모듈
# 모듈: 관련된 데이터와 함수를 하나로 묶은 단위
# random 모듈의 choice(데이터) 함수 사용
# : 호출되는 데이터 내에서 random 모듈이 임의로 선택하여 반환

# >> 사용 방법
# import random
# random.choice(데이터)

import random

# 가위, 바위, 보를 리스트(options)로 저장
# > 무한 루프 내에서 사용자로 부터 가위, 바위, 보 중의 입력을 받음
# > 사용자의 입력이 '종료'일 경우 게임을 종료(무한 루프의 종료)
# > 사용자의 입력이 options 리스트에 없는 경우
#   : 오류 메시지 출력 후 다시 조건 검사
# > options 내의 데이터가 입력된 경우 random의 선택과 비교하여
#   : 결과 반환

options = ['가위', '바위', '보']

while True:
    print("----------------------------------")
    print('가위, 바위, 보 게임 시작!')
    print('"종료"를 입력하면 게임이 종료됩니다.')
    user_choice = input('가위, 바위, 보 중 하나를 선택하세요.')

    if user_choice == '종료':
        print('게임을 종료합니다.')
        break

    if user_choice not in options:
        print('잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력하세요.')
        continue

    computer_choice = random.choice(options)
    print(f'컴퓨터의 선택 : {computer_choice}')

    if user_choice == computer_choice:
        print('무승부입니다.')
    elif (user_choice == '가위' and computer_choice == '보') or (user_choice == '바위' and computer_choice == '가위') or (user_choice == '보' and computer_choice == '바위'):
        print('사용자의 승리입니다.')
    else:
        print('컴퓨터의 승리입니다.')

# 숫자 맞추기 게임
# 1. 컴퓨터가 1부터 20 사이의 임의의 숫자를 하나 선택
# 2. 사용자에게 최대 5번의 기회가 주어짐
# 3. 사용자가 숫자를 입력하면
#    , 컴퓨터는 사용자의 입력이 정답보다
#    , 높은지, 낮은지, 정답인지 알려줌
# 4. 사용자가 정답을 맞추거나 또는 기회를 모두 소진할 경우 게임종료

# random.randint(a, b)
# : a와 b 사이의 임의의 정수를 반환 (a, b를 모두 포함)

secret_number = random.randint(1, 20)

print('1부터 20사이의 숫자를 맞춰보세요! (기회 5번)')

# 사용자에게 5번의 기회를 제공
for i in range(1, 6):
    print(f'{i}번째 시도: 숫자를 입력하세요')
    guess = int(input())

    print(f"시도 {i}: 숫자를 입력하세요. (비밀 숫자: {secret_number})")
    if guess < secret_number:
        print('정답보다 낮습니다.')
    elif guess > secret_number:
        print('정답보다 높습니다.')
    else: # 정답과 동일
        break

if guess == secret_number:
    print(f'축하합니다. {i}번 시도에 숫자를 맞추셨습니다.')
else:
    print(f'기회를 모두 소진하셨습니다. 정답은 {secret_number}입니다.')
