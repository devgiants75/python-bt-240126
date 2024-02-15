# 학생 - 사람의 클래스를 상속관계로 구현 #

# 부모 클래스
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '이(가)' + food + '를 먹습니다.')

# 자식 클래스
class Student(Person):

    def __init__(self, name, school):
        # super() 함수
        # : 자식 클래스에서 부모 클래스의 속성이나 메서드에 접근
        super().__init__(name) # 부모 클래스의 생성자를 호출
        self.school = school

    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부합니다.')

seungah = Student('이승아', '코리아IT아카데미')
seungah.eat('아이스크림')
seungah.study()

dokyung = Person('이도경')
dokyung.eat('초콜릿')
# dokyung.study() - Error

### 자식 클래스의 생성자 ###

# 부모 클래스 없이는 자식 클래스 구현 불가!
# : 자식클래스의 생성자를 구현할 때에는 반드시
# : 부모클래스의 생성자를 먼저 호출해야 한다.

class ParentClass:
    def __init__(self, name):
        self.name = name
        print(f'부모클래스의 생성자는 이름을 호출합니다: {self.name}')

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name) # 부모 클래스의 생성자 호출
        self.age = age
        print(f'자식 클래스의 생성자는 이름: {self.name}과 나이: {self.age}를 호출합니다.')

child = ChildClass('이승아', 28)
# 자식 클래스 생성자 호출 시
# super()함수로 인해 부모 클래스의 생성자도 같이 호출

# 자식 클래스의 자료형태

# 부모 클래스의 객체는 부모 클래스의 인스턴스
# 자식 클래스의 객체는 자식 클래스의 인스턴스이면서 동시에 부모 클래스의 인스턴스

# - 어떤 객체가 어떤 클래스의 인스턴스인지 확인하는 함수
# isinstance(객체, 클래스): 결괏값을 불리언(Boolean) 값으로 반환

print(isinstance(child, ChildClass)) # True
print(isinstance(child, ParentClass)) # True

parent = ParentClass('이도경')
print(isinstance(parent, ChildClass)) # False
print(isinstance(parent, ParentClass)) # True