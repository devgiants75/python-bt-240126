# 파이썬 컬렉션 자료형 - 딕셔너리

# 딕셔너리(dictionary, dict)
# : 키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료형
# 변경O, 키 중복X - 값 중복O
# 순서가 없지만, 삽입 순서가 유지
# 데이터를 다양한 타입으로 지정 가능

# 딕셔너리 생성
# 1. 중괄호 {}로 표현, 각 항목은 콜론(:)으로 키와 값을 구분
# 2. dict() 함수를 사용하여 생성(각 항목을 =로 구분)
dict1 = {} # 빈 딕셔너리
dict2 = {'name': '이승아', 'age': 29, 'city': 'Busan'}
dict3 = dict(name='이도경', age=30, city='Busan')

# 딕셔너리 활용
# 1. 요소 추가/수정/삭제
# : 키를 사용하여 값을 검색
# 딕셔너리명[키값]

# 요소 접근
print(dict3['name'])
dict3['name'] = '이도갱'

# 요소 수정
print(dict3['name'])

# 요소 추가
# 딕셔너리명['새로운키'] = 새로운값
dict3['height'] = 157
print(dict3)

# 요소 제거
# del 딕셔너리명['키']
del dict3['city']
print(dict3)