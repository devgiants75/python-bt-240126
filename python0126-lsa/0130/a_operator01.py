#! 연산자(operator)
# : 특정 작업을 수행하는데 사용되는 특수 기호나 구문

#! 연산자의 종류
# 항목의 개수
# - 단항, 이항, 삼항 연산자로 구분
# 단항 ex) 1, a, "안녕"
# 이항: 연산자가 한 개 있는 구문 ex) a = 1, msg = "안녕"
# 삼항: 연산자가 두 개 있는 구문 ex) a + b = 3

# 사용 목적
# - 산술, 대입, 관계, 논리 연산자로 구분

# 1. 산술 연산자
# : 기본적인 수학 연산을 수행
# 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# 거듭제곱(**), 몫(//), 나머지(%)

a = 5
b = 3
print(a + b) # 8
print(a - b) # 2
print(a * b) # 15
print(a / b) # 1.666666667
print(a ** b) # 5 * 5 * 5 = 125
print(a // b) # 1
print(a % b) # 2

# 2. 대입 연산자 (할당 연산자)
# : 변수에 값을 할당하는 데 사용
# - 기본 대입 연산자: =
# - 복합 대입 연산자: +=, -=, *=, /=

a = 10 # 10을 a에 대입

a += 5 # a = a + 5
print(a) # 15

a -= 3 # a = a - 3
print(a) # 12

a *= 2 # a = a * 2
print(a) # 24

a /= 3 # a = a / 3
print(a) # 8.0

# 3. 비교 연산자 (관계 연산자)
# : 두 값의 관계를 비교하는 데 사용
# : 결과값이 boolean(논리) 타입으로 반환
# 이상(>=), 이하(<=), 초과(>), 미만(<)
# 동등(==), 부등(!=)

a = 10
b = 20
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

# 4. 논리 연산자
# : boolean(참/거짓)의 값에 대한 논리적인 연산을 수행
# : and(논리곱), or(논리합), not(논리부정)

a = True
b = False

# and(논리곱)
# : 모든 조건이 True일 때 True를 반환
# : False가 하나라도 존재하면 False를 반환
print("--- 논리 연산자 결과값 ---")
print(a and b) # False
print(a and a) # True

# or(논리합)
# : 적어도 하나의 조건이 True일 때 True를 반환
# : 모든 조건이 False일 때만 False를 반환
print(b or a or b) # True
print(a or a) # True

# not(논리부정)
# : boolean값을 반전
print(not a) # False
print(not b) # True