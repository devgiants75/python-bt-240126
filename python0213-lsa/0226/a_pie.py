### matplotlib 라이브러리 ###

#! pie() 함수
# : 원형 그래프(파이 차트)를 작성하는 함수
# : 전체에 대한 각 부분의 비율을 시각적으로 표현

import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(121)

data = [1, 2, 3]
axes1.pie(data)

# 형태가 타원이 아닌 일반 원의 형태로 출력될 수 있도록 설정
plt.axis('equal')

plt.show()

# pie()함수의 매개변수
# - labels: 각 섹션의 라벨 설정
# - colors: 각 섹션의 색상 설정
# - shadow: 섹션에 그림자 추가

figure = plt.figure()
axes2 = figure.add_subplot(111)

data = [1, 2, 3, 4, 5]
labelData = ['A', 'B', 'C', 'D', 'E']
colorsData = ['red', 'orange', 'green', 'yellow', 'blue']

axes2.pie(data, labels=labelData, colors=colorsData, shadow=True)

plt.title('Pie Chart')
plt.show()