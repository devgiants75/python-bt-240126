### matplotlib 라이브러리의 한글 처리 ###

# font-manager & rc를 이용하여 사용하고자 하는 한글 폰트 등록
# 'C:\\Windows\\Fonts\\HMFMPYUN.TTF'

# font-manager, rc는 폰트 설정 관련 기능을 제공
from matplotlib import font_manager, rc
# 그래프를 그릴 페이지 제작을 위한 기능 제공
import matplotlib.pyplot as plt
import matplotlib

# 폰트 경로 직접 지정
font_path = 'C:\\Windows\\Fonts\\HMFMPYUN.TTF'

# 폰트 이름 가져오기
font_name = font_manager.FontProperties(fname=font_path).get_name()
# matplotlib과 rc 함수를 사용해 폰트 설정
matplotlib.rc('font', family=font_name)

# 데이터와 함께 한글 라벨 지정
plt.plot(['봄', '여름', '가을', '겨울'], [20, 30, 15, 10])
plt.title('한글 깨짐 방지') # 그래프 제목에 한글을 사용
plt.show() # 그래프 표시