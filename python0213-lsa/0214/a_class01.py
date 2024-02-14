### 객체 & 클래스 정의 ###

#! 객체란?
# : 서로 많은 데이터를 하나로 묶어서 표현한 것
# : 현실 세계의 사물이나 개념을 프로그램 내에서 표현한 것

# EX) 웹 페이지에 작성할 '게시글'
# : 게시글 번호, 작성자, 제목, 내용, 작성일자, 수정일자, ... 등
# >> 데이터(속성)
# : 위 데이터를 처리하는 기능
# >> 기능(메서드)

#! 클래스란?
# : 객체를 만드는 도구
# : 객체를 생성하기 위한 설계도 또는 틀
# : 클래스를 정의하면 해당 클래스에 속한 객체들이 가져야할
#   속성과 메서드를 명시

# 붕어빵(객체) & 붕어빵 틀(클래스)
# : 같은 클래스로 만든 객체라도 각각의 객체는 서로 다른 값을 가짐

#! 인스턴스란?
# : 클래스에 의해 생성되어 '메모리에 할당'된 객체
# : 클래스로부터 객체를 생성하는 과정 >> 인스턴스화

# 붕어빵 틀 클래스로 만든 붕어빵은 객체(object)
# 붕어빵은 붕어빵 틀로 만든 인스턴스(instance)
# : 객체 = 인스턴스

# '이승아'는 '사람' 클래스의 인스턴스
# 'BMW'는 '자동차' 클래스의 인스턴스
# '파이썬'은 '프로그래밍 언어' 클래스의 인스턴스
# '진라면'은 '라면' 클래스의 인스턴스

#! 클래스 정의
# == 클래스를 생성한다
# : class 키워드로 클래스를 정의
# : UpperCamelCase 규칙을 따름
#   첫글자 & 이어지는 단어의 첫 글자를 대문자로 작성

#? 파이썬 명명 규칙
# 변수, 함수, 파일명: snake_case (my_best_friend)
# 함수명: UpperCamelCase (MyBestFriend)

#! 클래스 기본 형식 - 들여쓰기 문법을 따름
'''
class 클래스명:
    본문(클래스의 상세 정의 - 속성, 메서드 등)
'''
# : 클래스 내부에는 데이터를 표현하는 속성(변수)
# : 클래스가 수행할 수 있는 행동을 정의하는 메서드(함수)를 포함

#! 객체 생성
# : 클래스 이름 뒤에 괄호를 붙여 호출하면
#   해당 클래스의 인스턴스(객체)가 생성
# 객체명 = 클래스명()

# 객체1 = 클래스명()
# 객체2 = 클래스명()

#! 클래스 정의와 객체 생성
class FishBread: # 붕어빵 틀 (클래스)
    pass # 아무런 정의 없이 클래스를 생성 (아무런 동작도 수행 X)

# FishBread 클래스의 인스턴스를 생성하고, bread 변수에 할당
bread = FishBread()
# bread (객체)
# FishBread (클래스)

print(bread)
# <__main__.FishBread object at 0x00000213C6A95880>
# : 클래스의 인스턴가 메모리 상의 특정 주소에 할당
# : 객체가 저장된 메모리의 주소