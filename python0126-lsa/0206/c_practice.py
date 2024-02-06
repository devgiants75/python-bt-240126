# 1. 'Hello, World!'를
# 출력하는 함수를 작성
def hello_world():
    print('Hello World!')
hello_world()

# 2. 주어진 두 숫자의 합을 (3, 2)
# 반환하는 함수를 작성
def add(a, b):
    return a + b
print(add(3, 2))

# 3. 주어진 숫자 리스트의 합을 ([1, 2, 3, 4, 5])
# 반환하는 함수를 작성
def sum_array(numbers):
    return sum(numbers) # 리스트의 내부 모든 요소의 합을 반환하는 sum
print(sum_array([1, 2, 3, 4, 5])) # 15

# 4. 이름을 인자로 받아
# 인사하는 함수를 작성
# 만약 이름이 주어지지 않은 경우,
# "Guest"라는 이름으로 인사
def greet(name="Guest"):
    print(f'Hello, {name}')
greet('이승아')
greet()