### 파일 복사 예제 ###
# 이미지 파일을 복사

# 원본 이미지는 프로젝트 루트 디렉토리에 이미지를 저장
# : python-workspace

image_size = 1024
# 복사본은 0208폴더 내에 저장
with open('../../puppy-2785074_1280.jpg', 'rb') as source:
    with open('../../copy_image.jpg', 'wb') as copy:
        while True:
            buffer = source.read(image_size)
            if not buffer: break
            copy.write(buffer)
print('copy_image.jpg 파일이 복사되었습니다.')