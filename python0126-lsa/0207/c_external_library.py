### 파이썬 외부 라이브러리 ###

# 파이썬 외부 모듈 설치 및 사용
# : pip를 통해 외부 모듈을 설치

#! pip
# : 파이썬으로 작성된 패키지(라이브러리)를 관리하는 시스템
# : 파이썬 설치 시 자동으로 설치

#! pip 환경변수 등록
# 1. 파일 탐색기
# 2. C:\Python312\python.exe -m pip install numpy

#! pip 기본 명령어
# >> cmd(명령 프롬프트)츠

# 1. pip list
# : 현재 설치되어 있는 외부 모듈의 리스트를 보여주는 명령어
# 2. pip install 패키지명
# : 해당 패키지 설치 명령어
# 3. pip uninstall 패키지명
# : 해당 패키지 삭제 명령어

#! 외부 모듈(라이브러리) 사용 방법
# : 일반 표준 모듈 사용법과 동일
# : import, from import, import as 모두 사용 가능

### 파이썬 외부 모듈 - numpy ###
# : 수치 연산 라이브러리
# : 대규모 다차원 배열 & 행렬 연산에 필요한 함수를 제공

# 파이참에서 외부 모듈 & 패키지 설치 시 alt enter shift
import numpy as np

# 1. 1차원 배열 생성
# np.array([요소1, 요소2, 요소3 ...])
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2. 2차원 배열 생성
# np.array(([요소1, 요소2, ...], [요소1, 요소2, ....]))
arr2 = np.array(([1, 2, 3], [4, 5, 6]))
print(arr2)

# 3. 배열의 형태 확인
# : 배열명.shape
print(arr2.shape) # (2, 3) >> 2행 3열

# 4. 배열 연산
# : 배열의 모든 요소에 대한 연산식이 가능
arr3 = arr + 2 # 배열의 모든 요소에 2의 값을 더해서 출력
print(arr3)

# 5. 통계 함수 사용
# >> 엑셀에서 사용하는 함수식 사용이 가능
print(np.mean(arr)) # 넘파이 배열의 평균값 - 3.0
print(np.sum(arr2)) # 넘파이 배열의 총합 - 21

### 파이썬 외부 모듈 - pandas ###
# : Python Data Analysis Library의 약자
# : 파이썬에서 데이터 분석을 위해 사용되는 라이브러리

#! 파이참을 사용한 외부 라이브러리 설치
# 1. 왼쪽 상단의 햄버거 메뉴바 > File > Settings (ctrl + alt + s)
# 2. Project <프로젝트이름>
# : Python Interpreter를 선택
# : 현재 프로젝트에 설정된 Python 인터프리터와 설치된 패키지 목록 확인

# 3. 화면 왼쪽 상단의 + 버튼 클릭
# : 패키지 설치 화면 확인 > 검색 바에서 패키지 검색 후
# : 왼쪽 하단의 패키지 설치 버튼 클릭

# pandas DataFrame 생성
# : 여러 개의 컬럼으로 구성된 2차원의 데이터 구조 (표)

import pandas as pd

# DataFrame 생성
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

# 데이터 엑세스: 특정 데이터에 접근
# column 접근 (세로)
print(df['A']) # A의 값을 인덱스 번호로 나누어서 출력

# row 접근 (가로)
# DataFrame명.loc[인덱스번호]: 해당 인덱스 번호의 데이터를 출력
print(df.loc[1])