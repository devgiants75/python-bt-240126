#! 파이썬 메서드 - 문자열

# .format()
# .count()
# .find()
# .index()
# .upper(), .lower(), .capitalize(), .title()

# join()메서드
# : '문자열 리스트'를 하나로 합쳐 하나의 문자열로 변환
# : 해당 요소들을 구분짓는 문자(기호 포함)를 지정 가능
fruits = ['apple', 'orange', 'banana']
# apple, orange, banana
print(', '.join(fruits))
print(''.join(fruits))

# split() 메서드
# : 하나의 문자열에서 문자열을
# 특정 문자(기호)를 기준으로 분리하여 리스트를 생성

# : 기호와 공백 모두 문자로 인식
# apple, orange, banana
fruits = 'apple, orange, banana'

print(fruits.split(', ')) # ['apple', 'orange', 'banana']

# replace()
# : 특정 문자나 문자열을 다른 문자나 문자열로 교체
# 'Hello, World' >> 'Hello Python'
# : 첫 번째 인자 - 변경할 문자나 문자열
# : 두 번째 인자 - 새로운 문자나 문자열
# 인자
# : 함수(기능)에서 사용할 데이터
message = 'Hello World'
print(message.replace('World', 'Python'))

# strip() 메서드 (lstrip, rstrip)
# : 불필요한 문자열을 제거(공백)
message = '   Hello   '

# 문자열 양쪽 끝의 공백 및 다른 특정 문자를 제거
print(message.strip())
print(message.lstrip()) # 문자열 왼쪽
print(message.rstrip()) # 문자열 오른쪽
