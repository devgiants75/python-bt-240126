# 파이썬 반복문 예제 #

#! 1. 1부터 10까지 합을 구하는 프로그램 작성
# >> for 반복문과 산술 연산자 사용

# 합계를 저장할 변수 total을 0으로 초기화
total = 0

# for 반복을 사용하여 1부터 10까지를 합산
for i in range(1, 11):
    total += i # total = total + i

# 최종합계 출력
print(total)

#! 1부터 5 사이에 존재하는 모든 정수를 역순으로 출력
# range()의 역순 정의는: range(시작수, 끝수, 간격-음수)
for i in range(5, 0, -1):
    print(i)

# 사용자로부터 양의 정수를 입력받고
# , 해당 숫자만큼 과일 이름을 입력받아 basket 리스트에 저장

# 사용자로부터 양의 정수 입력
num_of_fruits = int(input('입력할 과일의 개수를 입력하세요: '))

# basket 빈 리스트 생성
basket = []

# 입력받은 숫자만큼 반복하면서 과일 이름을 입력받고 리스트에 추가
for i in range(num_of_fruits):
    fruit = input('과일 이름을 입력하세요: ')
    basket.append(fruit)
print('과일 바구니 : ', basket)

# 3. for문 사용: 1부터 10까지의 짝수만 출력하는 프로그램
# >> range() 함수를 사용하여 간격 조절
for i in range(2, 11, 2):
    print(i)

# >> if 조건식을 사용한 출력
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# while문의 무한 루프를 사용하여
# 사용자로부터 받는 입력 값에 따라 다른 로직이 실행되는 프로그램
# : 숫자를 입력

# 1. 숫자가 아닌경우: 숫자를 입력해주세요.
# if not userInput.isdigit():
    # print('숫자만 입력해주세요.)
# 2. 1을 입력: 로그인
# 3. 2를 입력: 회원가입
# 4. 3을 입력: 게임시작
# 5. 0을 입력: 게임종료 - break

while True:
    print('로그인: 1, 회원가입: 2, 게임시작: 3, 게임종료: 0')
    userInput = input('숫자를 입력해주세요.')

    # 숫자가 아닌 경우
    if not userInput.isdigit():
        print('숫자만 입력해주세요.')
        continue

    # 숫자를 입력한 경우
    numberInput = int(userInput)

    if numberInput == 1:
        print('로그인')
    elif numberInput == 2:
        print('회원가입')
    elif numberInput == 3:
        print('게임시작')
    elif numberInput == 0:
        print('게임종료')
        break
    else:
        print('알 수 없는 명령입니다. 다시 입력해주세요')
