### 정적 메서드 ###

#! 1. 정적 메서드
# : @staticmethod 데코레이터를 사용하여 정의된 메서드
# : 클래스나 인스턴스의 상태를 수정하거나 접근하지 않는 메서드
# : 클래스나 인스턴스의 정보에 접근하지 X

#! 2. 정적 메서드의 특징
# : 인스턴스 객체 없이도 호출 가능 (클래스 이름을 통해 호출 가능)
# : 클래스나 인스턴스의 상태와 무관한 독립적인 로직 수행 시 사용

# 인스턴스 메서드 - 첫 번째 매개변수로 self를 전달
# 생성자 메서드 - __init__ (첫 번째 매개변수로 self를 전달)
# 클래스 메서드 - 첫 번째 매개변수로 cls를 전달
# 정적 메서드 - 필수 매개변수 X

class MyClass:
    class_var = '클래스 변수'

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    # 필수 매개변수 필요 X, 일반 선택 매개변수 가능
    def static_method(param1, param2):
        return param1 + param2

print(MyClass.class_method())
print(MyClass.static_method(5, 7))

# 정적 메서드 예제
class Korean:
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagin your Korea')

Korean.slogan()