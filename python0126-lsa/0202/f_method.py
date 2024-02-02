# 파이썬의 메서드 #

# method(메서드, 메소드)
# : 특정 객체를 통해서만 호출할 수 있는 함수

# 1. 문자열 메서드
# format() 메서드: 문자열에 변수를 삽입 or 형식을 지정하는데 사용
print('Hello, {}. I am {} years old'.format('lsa', 28))

# count() 메서드: 특정 문자나 문자열이 등장하는 횟수를 세는 데 사용
print('Hello, Python'.count('o')) # 2

# find() 메서드: 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
# : 찾고자하는 문자나 문자열이 없는 경우 -1을 반환
print('Hello, Python'.find('o')) # 4
print('Hello, Python'.find('w')) # -1

# index() 메서드: 특정 문자나 문자열이 처음 등장하는 인덱스를 반환
# : 찾고자하는 문자나 문자열이 없는 경우 ValueError가 발생
print('Hello, Python'.index('o')) # 4
# print('Hello, Python'.index('w')) # ValueError

# 대소문자 변환 메서드
# .upper(): 모든 소문자를 대문자로 변환
# .lower(): 모든 대문자를 소문자로 변환
print('hello, python'.upper()) # HELLO, PYTHON
print('HELLO, PYTHON'.lower()) # hello, python
print('hello, python'.capitalize()) # 첫글자만 대문자, 나머지는 소문자
print('hello, python'.title()) # 각 단어의 첫 글자를 대문자, 나머지 소문자
