# 파이썬 모듈

#! 모듈(module)
# : 함수나 변수 또는 클래스 등을 모아 놓은 파일
# : .py 확장자를 가진 파이썬 파일
# : 재사용 가능한 코드 블록을 만들어 다른 파이썬 프로그램에서 사용

#! 모듈의 필요성
# 1. 코드의 재사용성
# : 한 번 작성하면 계속해서 재사용 가능
# : 개발 시간 단축 & 코드의 일관성 유지 용이

# 2. 코드의 구조화
# : 코드의 유지보수 용이 & 코드의 이해도가 높아짐

#! 파이썬 모듈의 사용 방법
# import 키워드를 사용하여 '불러오기' 가능
# : .py 확장자를 생략하여 파일명만 작성

# f_my_module을 불러와서 사용

import f_my_module

# import한 모듈 사용 방법
# 모듈명.함수명
print(f_my_module.add(3, 5)) # 8
print(f_my_module.sub(3, 5)) # -2

# from import 사용
# from 모듈명 import 항목명(변수, 함수, 클래스명)
# : 특정 모듈에서 하나 이상의 특정 항목만 불러오기 가능
# : 항목을 사용할 때 모듈명을 접두어로 붙이지 않아도 사용 가능

# 여러 항목을 동시에 불러오는 경우
# : 쉼표(,)를 사용하여 나열 가능
from f_my_module import greet, info, my_variable
print(greet('이승아'))
print(info(28))
print(my_variable)

# import as 사용
# : 모듈의 이름이 길거나 다른 모듈과 충돌할 가능성이 있는 경우
# : 모듈에 대한 별칭(alias)을 지정하는 방법

import f_my_module as mm
print(mm.add(5, 7))
print(mm.sub(5, 7))

from f_my_module import greet as hello
print(hello('이승아'))