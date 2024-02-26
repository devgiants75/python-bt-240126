### 워드 클라우드 ###

#! 워드 클라우드(word cloud)
# : 텍스트 데이터에서 자주 등장하는 단어를
#   시각적으로 표현하는 외부 라이브러리
# : 소셜미디어 분석, 설문조사 결과 분석 등에 사용

#! 라이브러리 설치
# : pip install wordcloud

#! wordcloud 생성
import wordcloud
import matplotlib.pyplot as plt

#! 여러분들이 사용하시는 프로그래밍 언어는 무엇인가요?
# 43명이 설문조사에 참여
words = {
    'Python': 16,
    'Java': 5,
    'C': 7,
    'C++': 9,
    'JSP': 6
}

# 워드클라우드 생성
# wordcloud.WordCloud()
wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(words)

plt.figure()
plt.imshow(cloud)
plt.show()

### 워드 클라우드에서의 한글 사용 ###
programmings = {
    '파이썬': 20,
    '빅데이터': 5,
    '웹크롤링': 7,
    '인공지능': 9,
    '딥러닝': 12
}

# 한글 폰트 경로를 가져오기
# 파일 탐색기 > c드라이브 > Windows 폴더 > Fonts 폴더
# : 사용하고자 하는 폰트 우클릭 > 속성
# : 위치정보\폰트명.확장자
# C:\Windows\Fonts\H2PORM.TTF
#
wc = wordcloud.WordCloud(font_path='C:\\Windows\\Fonts\\H2PORM.TTF')
cloud = wc.generate_from_frequencies(programmings)

plt.figure()
plt.imshow(cloud, )
plt.show()