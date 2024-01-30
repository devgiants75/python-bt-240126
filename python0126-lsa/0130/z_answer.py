# hours, minutes, seconds

# 초를 입력받습니다.
total_seconds = int(input("초를 입력하세요: "))

# 입력받은 초를 시, 분, 초로 변환합니다.
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# 결과를 출력합니다.
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")