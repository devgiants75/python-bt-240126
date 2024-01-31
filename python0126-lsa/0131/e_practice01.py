# 1. 사용자로부터 입력 받은 숫자가 짝수인지 홀수인지 판별하는 프로그램
# num 변수에 사용자로부터 숫자를 입력받기 : input
# # 입력받은 숫자가 짝수인지 홀수인지 판별 : if-else

num = int(input('숫자를 입력해주세요.'))

if num % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# 2. 중첩 조건문을 이용한 성적 분류 프로그램

# score 변수에 사용자로부터 숫자를 입력받기 : input
score = int(input('성적을 입력하세요(0 ~ 100): '))

# 성적이 유효한 범위인지 확인
# - 0미만 100초과의 경우(유효하지 X) '오류' 메시지 출력
# - 성적이 유효한 경우 성적에 따라 등급을 분류
#   (90점 이상 A, 80점 이상 B, 70점 이상 C, 그 외에는 F)
# - 해당 등급을 grade 변수에 할당하여 출력

if score < 0 or score > 100:
    print('잘못된 성적입니다.')
else:
    # 올바른 성적(0~100) - 성적에 따라 등급 분류
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'

    print(f'당신의 등급은 {grade}입니다.')
