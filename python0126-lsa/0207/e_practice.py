# 파일 입출력 예제 #
# p.237

# 엄마돼지 아기돼지 동요 가사가 적힌 pig.txt를 열어서
# 해당 텍스트 파일에 '꿀'이라는 글자가 몇 번 나오는지 찾는 프로그램

file = open('pig.txt', 'rt', encoding='utf-8')

# 각 줄을 리스트로 저장
line_list = file.readlines()

# 리스트의 반복을 통해 조건문에 '꿀'과 같으면 count를 증가 할당
count = 0
for line in line_list: # 33번 반복(33개의 줄)
    for word in line: # 각 줄을 구성하는 각 문자를 순회
        if word == '꿀':
            count += 1
print(f'꿀은 전체 {count}번 나타납니다.')

#### 외부 파일 사용 방법 강의 ####