# 파이썬의 가변 인자

# 가변 인자
# : 임의의 개수의 인자를 받는 인자

# 표기법
# : 매개변수명 앞에 *표시를 붙임
# : 관례적으로 매개변수명을 args로 사용 (argument)

# 사용법
# : 함수 내에서 args는 튜플로 처리 (순서O, 변경X, 중복O)

def print_args(*args):
    for arg in args:
        print(arg)

print_args('Hello', '안녕', '니하오', '오하이오')
print_args(1, 2, 3, 4, 5)