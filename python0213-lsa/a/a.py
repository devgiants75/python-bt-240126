import requests
from bs4 import BeautifulSoup

# 네이버 웹툰 페이지에 요청을 보냅니다.
url = 'https://comic.naver.com/webtoon'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

# 요청이 성공적으로 수행되었는지 확인합니다.
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 수정된 class 명으로 div 태그를 찾습니다.
    daily_divs = soup.find_all('div', class_='WeekdayMainView__daily_all_item--DnTAH')

    # 확인을 위한 출력: daily_divs의 길이를 출력합니다.
    print(f"Found {len(daily_divs)} daily divs.")

    # 각 요일별로 웹툰의 수를 계산합니다.
    webtoon_counts = {}
    days = ['월', '화', '수', '목', '금', '토', '일']
    for i, daily_div in enumerate(daily_divs):
        # 각 div 태그 내에 있는 ul 태그들을 찾습니다.
        webtoon_lists = daily_div.find_all('ul')
        # 각 ul 태그 내의 li 태그들의 수를 합산합니다.
        webtoon_count = sum(len(ul.find_all('li')) for ul in webtoon_lists)
        # 요일별 웹툰의 수를 저장합니다.
        webtoon_counts[days[i]] = webtoon_count

        # 요일별 웹툰의 수를 한글로 출력합니다.
        for day in days:
            if day in webtoon_counts:
                print(f"{day}요일의 웹툰 수: {webtoon_counts[day]}")
        else:
            print(f"{day}요일의 웹툰 수 정보를 찾을 수 없습니다.")
else:
    print('웹페이지를 가져오는데 실패했습니다.')