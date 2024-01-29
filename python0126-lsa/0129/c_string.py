# 파이썬 문자열 구조 확인
message = "I like you!"

# 1. 문자열 길이
# : len()
# : 문자열의 길이를 구하는 파이썬 내장 함수(기능) - length
# : 파이썬의 경우 띄어쓰기(공백)와 기호를 문자로 포함
print(len(message)) # 11

# 2. 문자열 인덱싱
# : 문자열 내의 특정 위치의 문자에 접근하는 방법
# : 인덱스 번호는 0부터 시작(왼쪽)
# : 음수 인덱스 번호(-1부터 시작)는 문자열의 끝에서 시작(오른쪽)

# 문자열 전체 인덱스 번호는 문자열 길이 - 1
# 인덱싱 방법
# : 변수명[인덱스번호]
print(message[0]) # I
print(message[5]) # e
print(message[10]) # !
print(message[-1]) # !

# 3. 문자열 슬라이싱
# : 문자열 안의 단어(부분 문자열)를 뽑아내는 역할
# 슬라이싱 방법
# : 변수명[시작번호:끝번호] (시작번호와 끝번호는 인덱스번호)
# : 슬라이싱의 경우 끝 번호를 포함 X
# ex) word[2:5] / 2 <= word < 5

# I like you!
print(message[2:5]) # lik
print(message[2:6]) # like

# 시작 인덱스 생략 시: 문자열의 시작부터 슬라이싱
# 끝 인덱스 생략 시: 문자열의 끝까지 슬라이싱
text = "Python programming"
print(text[:6]) # Python
print(text[7:]) # programming