### 파이썬 데이터 시각화 실습 ###

# 교재: p.348

# 시리얼에 포함된 비타민의 함량을 나타낸 그래프
# : 각 항목의 비율이 나타날 수 있도록 그래프로 표시
# : pie()차트 생성

# 비타민 A: 0.18
# 비타민 B1: 0.3
# 비타민 B2: 3.33
# 비타민 B6: 0.38
# 나이아신: 3.75
# 비타민 C: 25
# 비타민 D: 0.25
# 비타민 E: 2.75
# 엽산: 0.1

# 라이브러리 가져오기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = 'C:\\Windows\\Fonts\\H2PORM.TTF'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터 설정
vitamins = ['비타민 A', '비타민 B1', '비타민 B2', '비타민 B6', '나이아신', '비타민 C', '비타민 D', '비타민 E', '엽산']
values =  [0.18, 0.3, 3.33, 0.38, 3.75, 25, 0.25, 2.75, 0.1]

# 파이 차트 생성
# : plt를 사용
plt.pie(values, labels=vitamins)
plt.title('시리얼에 포함된 비타민의 함량')
plt.legend(title='비타민 종류')
plt.axis('equal')

plt.show()