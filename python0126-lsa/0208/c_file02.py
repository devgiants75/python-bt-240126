### 파이썬 파일 입출력 ###

# 1. 파일 복사
# : 원본 파일(source)의 복사본 파일(copy)를 만드는 것

# 2. 파일 복사의 절차
# - 원본 파일 열기
# - 복사본 파일 생성
# - 원본 파일의 내용 읽기 & 복사본 쓰기
# : 원본 파일에서 한 번에 읽어들이는 데이터 크기를
# : 1KB(1024Byte)로 설정해 복사 프로그램을 구현
# - 파일 닫기(with문 사용 시 생략 가능)

# 픽사베이
# : 무료 이미지/동영상 다운로드 사이트

# robin_-_65801 (540p)

video_size = 1024 # 1024byte: 1KB

# 존재하는 비디오 파일을
with open('robin_-_65801 (540p).mp4', 'rb') as source:
    # copy_video.mp4를 생성하여 해당 문서에 복사
    with open('copy_video.mp4', 'wb') as copy:
        while True:
            # read(용량): 파일의 용량을 지정
            buffer = source.read(video_size)
            if not buffer:
                break
            copy.write(buffer)
print('copy_video.mp4 파일이 복사되었습니다.')