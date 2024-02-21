### 파이썬 시각화 예제 ###

# 라인 차트 생성하기
# : 시간의 경과에 따른 데이터의 변화를 보여주는 예제
# : 일주일 간의 온도 변화를 나타내는 차트

import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(2, 2, 1)

# 데이터 준비
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 18, 19, 20, 16, 14]

cities = ['NY', 'LA', 'CCG']
rainfall = [1200, 900, 850]

# 1행 2열의 subplot 구성
# : 각각의 축(ax1, ax2)를 반환
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 라인 차트 생성
# ax1(첫 번째 서브플룻) - plot() 라인 차트
ax1.plot(weeks, temperature)
# 서브플룻의 이름표 설정의 경우
# set_ 키워드를 각각의 이름표 앞에 작성
ax1.set_xlabel('Day')
ax1.set_ylabel('Temperature (C)')
ax1.set_title('Daily Temperatures in July')

# 막대 그래프 생성
# ax2(두 번째 서브플룻) - bar() 막대 차트
ax2.bar(cities, rainfall)
ax2.set_xlabel('City')
ax2.set_ylabel('Annual Rainfall (mm)')
ax2.set_title('Annual Rainfall by City')

# 그래프 표시
plt.tight_layout() # subplot 간 충돌 방지
plt.show()

