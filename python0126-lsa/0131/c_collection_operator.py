# 컬렉션 자료형의 연산

# 시퀀스(sequence) 자료형
# : 순서가 있는 자료형(리스트, 튜플, 문자열)

# 1. 시퀀스 연산자
# 결합(+), 반복(*) 연산자
result1 = [1, 2, 3] + [4, 5, 6]
print(result1) # [1, 2, 3, 4, 5, 6]

result2 = [1, 2] * 3
print(result2) # [1, 2, 1, 2, 1, 2]

# 2. 멤버십 연산자

list = [1, 2, 3, 4, 5]
str = "Hello, Python"

# in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함되어 있으면 True
# : , 그렇지 않으면 False를 반환
print(3 in list) # True
print(6 in list) # False

# not in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함되어있지 않으면 True
# : , 포함되어 있으면 False를 반환
print('Python' not in str) # False
print('Java' not in str) # True

# 연산자의 우선순위
result = (3 + 4) * 2 ** 2 > 10

# 1. 괄호 ()
# 2. 거듭제곱 **
# 3. 곱셈, 나눗셈, 나머지, 몫: *, /, %, //
# 4. 덧셈, 뺄셈