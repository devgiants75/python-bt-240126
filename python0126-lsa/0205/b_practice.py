# 다음 문자열에서 'apple'이 등장하는 횟수를 출력하시오
# : "apple banana apple cherry apple"
string1 = "apple banana apple cherry apple"
reduce_string = 'a b a c a'
print(string1.count('apple'))
print(reduce_string.count('a'))

# 다음 문자열에서 첫번째로 'banana'가 등장하는 위치를 출력하시오
# : "apple banana apple cherry apple"
print(string1.find('banana'))
print(string1.index('banana')) # 단어의 위치를 찾을 경우 단어의 시작 인덱스를 출력

# 다음 문자열을 모든 단어의 첫 글자가 대문자인 형식으로 변경하시오
# : 단어의 시작은 공백으로 구분
# : "apple banana apple cherry apple"
print(string1.title())

# 다음 문자열 리스트를 하나의 문자열로 합치시오
# : ['apple', 'banana', 'cherry']
string2 = ['apple', 'banana', 'cherry']
print(' '.join(string2)) # apple banana cherry
print(', '.join(string2)) # apple, banana, cherry

# 다음 문자열을 ','를 기준으로 분리하시오: "apple,banana,cherry"
# : 분리하여 리스트로 반환
string3 = "apple,banana,cherry"
print(string3.split(',')) # ['apple', 'banana', 'cherry']

# 다음 문자열에서 'python'을 'world'로 교체하시오: "Hello, python!"
string4 = 'Hello, python'
print(string4.replace('python', 'world')) # Hello, world

# 다음 문자열에서 양쪽의 공백을 제거하시오: " Hello, world! "
string5 = " Hello, world! "
print(string5.strip())