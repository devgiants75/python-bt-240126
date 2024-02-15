### 클래스 메서드 ###

# 1. 클래스 메서드 정의
# : 클래스에 속한 메서드
# : @classmethod 데코레이터를 사용하여 정의된 메서드

class MyClass:
    class_var = '클래스 변수'

    @classmethod
    def class_method(cls):
        return cls.class_var

# 2. 클래스 메서드 특징
# - 첫 번째 매개변수로 클래스 객체를 받는다. (cls 이름을 사용)
# - 인스턴스 객체 없이도 호출 가능
#   : 클래스 이름을 통해 호출 가능
#   : 인스턴스 & 클래스 호출이 모두 가능

class Korean:
    # 클래스 변수
    country = '한국'

    @classmethod
    def trip(cls, country): # cls-클래스객체, country-매개변수
        if cls.country == country: # Korean.country
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

# 국내 여행
Korean.trip('한국')
# 해외 여행
Korean.trip('미국')

# 클래스 변수 & 클래스 메서드 호출 시 유의사항
# 파이썬의 경우 인스턴스를 통해 클래스 변수에 접근할 때
# : 해당 이름의 인스턴스 변수를 먼저 검색
# : 인스턴스를 통해 클래스 변수에 값을 할당할 경우
# : 예기치 못한 인스턴스 변수가 생성 가능

#! 클래스 변수 값 변경 시에는 클래스로만 호출하여 값을 할당