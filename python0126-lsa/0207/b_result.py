# a_review.py 모듈을 사용 #

# 1. import
# : 변의 길이가 10인 정사각형의 넓이를 계산하고 출력
# : 반지름이 5인 원의 넓이를 계산하고 출력
import a_review # import 모듈명(파일명)

# import문으로 모듈을 가져오는 경우
# 모듈명.항목명으로 호출
result1 = a_review.calculate_square(10)
result2 = a_review.calculate_circle(5)
print(result1) # 100
print(result2) # 78.5

# 2. from import
# : a_review.py 모듈에서 calculate_square 함수만 import하여
# : 변의 길이가 7인 정사각형의 넓이를 계산하고 출력

from a_review import calculate_square
# from 모듈명(파일명) import 항목명(변수,함수,클래스)

# from import문으로 모듈을 가져오는 경우
# : 항목명으로만 기능 호출이 가능
result = calculate_square(7)
print(result) # 49

# 3. import as
# : a_review.py 모듈을 a라는 별칭으로 import하여
# : 반지름이 10인 원의 넓이를 계산하고 출력

import a_review as a
# import 모듈명(파일명) as 별칭

result = a.calculate_circle(10)
print(result) # 314.1