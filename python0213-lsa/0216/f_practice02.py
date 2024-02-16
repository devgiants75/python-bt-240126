### 예외 처리 & 클래스 ###

# 교재 p.306
# 우리나라의 모든 '도'를 맞히는 문제

# 지시사항
# 1. Quiz 클래스는 우리나라의 모든 도를 요소하는 리스트를 가짐(answer)
class Quiz:
    answer = ['경기도', '강원도', '충청도', '경상도', '전라도', '제주도']
# 2. Quiz 클래스는 challenge() 메서드를 가짐
# - 사용자의 입력을 처리하고 일치하는 정답이 있으면 '정답입니다.'를 출력
# - 해당 정답은 answer 리스트에서 제거
# - 다시 challenge() 메서드를 호출
# - 사용자의 정답이 틀린 경우 '틀렸습니다.'를 출력 (예외 메시지로 출력)
    @classmethod
    def challeng(cls):
        user_input = input('도를 입력하세요 : ')
        if user_input in cls.answer:
            cls.answer.remove(user_input)
            print('정답입니다.')
            if len(cls.answer) == 0:
                print('모든 도를 맞췄습니다. 성공입니다.')
                return
            cls.challeng()
        else:
            raise Exception('틀렸습니다.')

# 3. Quiz 클래스의 동작 확인
try:
    print('우리나라의 도를 맞춰보세요')
    Quiz.challeng() # 클래스 메서드
except Exception as e:
    print(e)

# 4. 정답을 모두 맞히는 경우 '모든 도를 맞췄습니다. 성공입니다.'를 출력