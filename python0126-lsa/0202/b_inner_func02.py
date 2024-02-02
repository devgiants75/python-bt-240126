# 파이썬 내장 함수

# 2. 숫자형 내장 함수

# - abs(x): 숫자의 절대값을 반환(부호X)
#           x 자리에 정수 또는 실수

print(abs(-5)) # 5
print(abs(+3.14)) # 3.14

# - divmod(a, b): a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(14, 4)) # (3, 2) >> 몫: 3, 나머지: 2

# - float(), int()
# : 문자열 또는 숫자를 실수, 정수로 변환

print(float(3)) # 3.0
print(int(3.14)) # 3

# max(iterable) & min(iterable)
# : 이터러블(iterable) 자료형 중에서 가장 큰 값을 반환

# iterable
# : 반복 가능한
# : string, list, tuple, set, dic 등

print(max([1, 2, 3, 4, 5])) # 5
print(max([234, 152, 234, 3465, 15])) # 3465

print(min([1, 2, 3, 4, 5])) # 1
print(min([234, 152, 234, 3465, 15])) # 15

# - pow(x, y): x의 y제곱한 결과를 반환
print(pow(2, 3)) # 8

# - round(number, n): 숫자를 n 소수점 자리까지 반올림한 결과를 반환
# n: 소수점자리 숫자, 생략 시 기본값 0
print(round(3.14159, 2)) # 3.14
print(round(3.14159)) # 3

# - sum(iterable, start)
# : iterable의 모든 항목과 시작값을 더한 결과를 반환
# start 생략 시 iterable값들만 더한 결과를 반환 (시작값 - 0)

print(sum([1, 2, 3, 4, 5])) # 15
print(sum([1, 2, 3, 4, 5], 10)) # 25
