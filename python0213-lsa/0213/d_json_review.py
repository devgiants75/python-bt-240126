# 파이썬 json 형식 사용 복습 예제 #

import json

# 초기 데이터 설정
data = {
    "name": "이승아",
    "age": 28,
    "hobbies": ["운동", "독서"]
}

# json 파일로 저장
filename = 'd_json_review.json'
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

#! json 파일 읽기 및 수정
# 1. json파일 읽어오기(json 모듈의 load 메서드 사용)
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# data의 데이터 중 hobbies 키의 값(리스트)에 데이터 추가
# 딕셔너리 자료의 값에 접근: 딕셔너리명[키]
data['hobbies'].append('코딩')

# 2. 수정된 데이터를 동일한 파일에 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 3. 수정된 파일 읽기 및 출력
with open(filename, 'r', encoding='utf-8') as f:
    updated_data = json.load(f)

print(updated_data)

# 4. json 파일에서 특정 데이터 조회
# json 형식이 파이썬의 딕셔너리 형태와 유사하기 때문에
# 데이터명[키]
print('Age: ', data['age'])
print('Name: ', data['name'])
print('Hobbies: ', data['hobbies'])