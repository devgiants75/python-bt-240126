### 클래스 변수 ###

# 1. 클래스 변수의 정의

# VS 인스턴스 변수
# : 인스턴스 마다 '서로 다른 값'을 가지는 경우에는 인스턴스 변수를 사용
# : 모든 인스턴스 변수들은 self 키워드를 붙여 사용
# EX) 사람 클래스 - 이름, 나이, 주소 등 (사람마다 다른 값)

#! 클래스 변수
# : 클래스 정의 내부에서 정의되지만 메서드 외부에서 선언되는 변수
# : 해당 클래스의 모든 인스턴스에서 '공유되는 값'을 저장
# : 메모리 공간 낭비를 막을 수 있다.
# EX) 한국 사람 클래스 - 소속 국가 (한국 사람이면 모두 같은 값)

class Korean:
    # 클래스 변수
    country = '한국'

    def __init__(self, name, age, address):
        # 인스턴스 변수 (self 키워드)
        self.name = name
        self.age = age
        self.address = address

person1 = Korean('이승아', 28, '부산시')
person2 = Korean('이도경', 30, '양산시')

# 인스턴스 변수 접근
# 인스턴스명.변수명
# - 해당 인스턴스에서만 접근 가능
print(person1.name)
print(person1.age)
print(person1.address)

print(person2.name)

# 클래스 변수 접근
# 클래스명.변수명 or 인스턴스명.변수명
print(person1.country)
print(person2.country)
print(Korean.country)

#! 클래스 변수의 값 변경
person2.name = '이현아'
print(person2.name)

# 클래스 변수의 값 변경 시
# : 해당 클래스의 모든 인스턴스에 대해 변경된 값이 반영

print(Korean.country) # 한국

Korean.country = '대한민국'
print(Korean.country) # 대한민국

person1.country = 'Korea'
print(person1.country)

# 인스턴스 변수 - 고유한 값 저장, 인스턴스를 통해서만 접근 가능
# 클래스 변수 - 공유되는 값 저장, 인스턴스 or 클래스로 접근 가능