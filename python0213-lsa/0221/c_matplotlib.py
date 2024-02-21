### matplotlib 라이브러리 ###

# matplotlib 라이브러리 사용
# : pyplot 모듈을 사용
# : 이름을 plt로 수정하는 import 형식을 사용
import matplotlib.pyplot as plt

#! figure & subplot
# 1. figure
# : 하나의 그래프 창을 나타냄
#   , 여러 개의 subplot을 포함할 수 있는 전체 영역
#     (한 figure 안에 여러 개의 subplot이 포함될 수 있음)
# - 사용법
# : plt.figure() 함수를 사용하여 Figure 객체를 생성
# : plt.figure(figsize=너비, 높이)를 사용한 크기 조절 가능 (선택)
figure = plt.figure(figsize=(8, 6)) # 너비가 8, 높이가 6인 Figure 생성

# 2. subplot
# : 실제로 그래프를 그리는 영역
# - 사용법
# : add_subplot() 함수를 사용하여 Figure 안에 Subplot을 추가
# : >> 3가지의 파라미터를 필요로 함
#      nrows: 그리드의 행 수
#      ncols: 그리드의 열 수
#      index: 그래프를 그릴 위치 (1부터 시작)

# 2행 2열의 subplot 생성
axes1 = figure.add_subplot(2, 2, 1) # 2행 2열 1번째 subplot
axes2 = figure.add_subplot(2, 2, 2) # 2행 2열 2번째 subplot
axes3 = figure.add_subplot(2, 2, 3) # 2행 2열 3번째 subplot
axes4 = figure.add_subplot(2, 2, 4) # 2행 2열 4번째 subplot

# 그래프를 출력
plt.show()

# 여러 개의 subplot을 동시에 생성: subplots()함수를 사용
axes = plt.subplots(nrows=3, ncols=3)
plt.show()