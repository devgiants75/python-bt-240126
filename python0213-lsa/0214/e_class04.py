### 생성자 ###

class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

satang = Candy() # 값이 없는 인스턴스를 생성
# print(satang.shape) - Error

satang.set_info('circle', 'red')
# >> 값을 저장할 수 있는 메서드를 따로 호출
print(satang.shape) # circle

#! 생성자를 이용한 인스턴스 생성
# 생성자
# : 인스턴스를 생성할 때 자동으로 호출되는 특별한 메서드
# : 주로 인스턴스 변수의 초기화 작업을 수행

#! 생성자의 형태
# __init__()
# : 파이썬에서 생성자의 이름은 반드시 __init__으로 고정! (변경 X)
# : 생성자의 첫 번째 매개변수도 반드시 self로 선언

# 파이썬에서 __(언더바 2개)로 시작되는 메서드들은
# : 미리 기능과 역할이 부여된 메서드

class Candy2:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

# 생성자를 사용한 객체 생성
# : 생성자가 자동으로 호출
# : __init__ 메서드명을 사용하지 않아도 됨
satang2 = Candy2('square', 'blue')
print(satang2.shape, satang2.color)

### 소멸자 ###
# : 인스턴스가 소멸될 때 자동으로 호출되는 메서드
# : 소멸 >> 메모리에서 삭제
# : __del__()

class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample() # Sample 클래스의 객체(인스턴스)

# 객체 삭제
# : del 키워드를 사용
# del 객체명
del sample

# 파이썬 소멸자 사용 시 주의사항
# : 소멸자(__del__메서드)는 객체가 메모리에서 제거될 때 호출
# : del 키워드를 사용하긴 하지만
# : 소멸자 자체의 삭제 시점을 프로그래머가 명확하게 지정 X
# >> 파이썬의 가비지 컬렉션이 언제 동작할지 불분명