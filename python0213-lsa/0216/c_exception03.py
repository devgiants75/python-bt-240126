### else문 & finally문 ###

# else문
# : try 블록에서 예외가 발생하지 않으면 처리되는 구문
# : 주로 정상적으로 코드가 실행되는 경우 수행할 작업을 정의
# : 반드시 except 블록 다음에 위치!

# finally문
# : 예외 발생 여부와 상관없이 try 구문이 종료될 때 항상 실행

# try:
#   코드 작성 영역
# except 예외명 as 변수명:
#   예외 발생 시 처리 영역 (변수명 출력)
# else:
#   예외가 없을 때 처리 영역
# finally:
#   언제나 실행되는 영역

#! else문 예제
try:
    number = int(input('정수를 입력하세요: '))
except ValueError as e:
    print(e) # invalid literal for int() with base 10: 'hello'
else:
    print(f'입력한 숫자는 {number}입니다.')
finally:
    print('프로그램을 종료합니다.')

#! finally문 예제

file = None # file의 변수를 이름 짓지만 아무것도 들어있지 않음을 의미

print('---finally문 예제---')
try:
    file = open('file2.txt', 'rt', encoding='utf-8')
    content = file.read()
    print(content)
except FileNotFoundError as m1:
    print(m1) # 읽어올 파일이 존재하지 않는 경우 발생
except Exception:
    print('파일 오류') # 예기치 못한 예외 처리
finally:
    if file: # file 객체가 정의되었는지 확인 - 존재할 경우에만
        file.close()
        print('파일을 닫습니다.')
    else:
        print('닫을 파일이 없습니다.')