# 파이썬의 지역 변수 & 전역 변수

#! 지역(local) 변수
# : 특정 함수 또는 메서드 내부에서 선언된 변수
# : 함수 내에서 정의, 오직 그 함수 내에서만 접근 가능한 변수
# : 함수가 종료되면 그 변수의 생명 주기도 끝남

def my_function():
    local_variable = 5 # 지역 변수 선언
    print(local_variable)

my_function() # 5 - 지역 변수 데이터 출력
# print(local_variable) - Error (함수 외부의 접근 불가)

#! 전역(global) 변수
# : 함수 외부에서 선언, 프로그램 전체에서 접근할 수 있는 변수
# : 함수 내부에서 전역 변수를 사용하려면 global 키워드를 사용해 선언
# >> 전역 변수의 접근은 global 키워드 없이 사용 가능

global_var = "I'm a global varible"

def my_function2():
    # 단순히 전역변수의 값을 참조하는 경우
    print(global_var)

my_function2()
print(global_var)

# global 키워드
# : 함수 내부에서 전역 변수의 값을 변경하고자 할 때
# : 해당 키워드 미지정 시 같은 이름의 새로운 지역변수가 생성
a = 0
def my_function3():
    # global 선언 전에는 새로운 지역변수로 인식되기 때문에
    # : 변수의 선언부를 확인할 수 X
    global a # 전역변수를 사용함을 명시
    a += 5 # a = a + 5
    print(a)

my_function3() # 5
print(a) # 5
my_function3() # 10
print(a) # 10