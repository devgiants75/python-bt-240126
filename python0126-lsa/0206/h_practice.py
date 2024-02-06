# 수학 퀴즈 게임
# : 사용자에게 랜덤으로 생성된 수학 문제(덧셈, 뺄셈, 곱셈)
# : 사용자가 정답을 입력하면 정답 여부를 알려줌
# math, datetime, random 라이브러리

import random
import datetime
def generate_quesition():
    # 연산식 중 하나를 랜덤으로 선택
    operations = ['+', '-', '*']
    operation = random.choice(operations)

    # 두 개의 숫자를 랜덤으로 생성
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # 선택된 연산에 따라 정답 계산
    if operation == '+':
        correct = num1 + num2
    elif operation == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2

    quesition = f'What is {num1} {operation} {num2}'
    return quesition, correct

def ask_quesition():
    # 해당 함수 호출 시 자동으로 generate_quesition()함수 호출
    question, correct = generate_quesition()
    print(question)
    start_time = datetime.datetime.now()

    user_answer = int(input('Your answer: '))

    end_time = datetime.datetime.now()
    # 시간 단위를 초단위로 계산
    time_taken = (end_time - start_time).total_seconds()

    if user_answer == correct:
        print(f'정답입니다. {time_taken}초 걸렸습니다.')
        return True, time_taken
    else:
        print(f'틀렸습니다. 정답은 {correct}입니다.')
        return False, time_taken

def play_math_quiz():
    # 게임을 무한 반복하여 사용자에게 게임의 중단 여부를 확인
    continue_playing = True
    while continue_playing:
        correct, time_taken = ask_quesition()
        if not correct:
            continue
        print('Do you want to play again? (yes/no)')
        response = input().strip().lower()
        if response != 'yes':
            continue_playing = False

    print('게임을 종료합니다.')

play_math_quiz()