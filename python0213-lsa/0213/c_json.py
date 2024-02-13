### 파이썬 JSON 파일 입출력 ###

# 1. JSON 파일?
# : JavaScript Object Notation의 약자
# : 키-값의 쌍으로 이루어진 데이터 형식 (파이썬의 딕셔너리 타입)
# - 자바스크립트에서 객체를 생성하는 방법과 유사하지만, 언어 독립적
#   : JSON 형식이 다양한 프로그래밍 언어에서 사용 가능

# 2. 파이썬에서 JSON 파일 생성
# : json 모듈 사용
# : dump() 메서드
# - python 데이터를 JSON 문자열로 변환하고 파일에 저장
# - json.dump(데이터, 데이터를 담을 파일 객체)

import json

# json 형식
# : 이름/값 쌍의 모음, 순서가 있는 값의 목록(리스트), 단순한 값의
# : 조합으로 구성
data = {
    "이름": "홍길동",
    "나이": 25,
    "주소": {
        "도시": "부산",
        "국가": "대한민국"
    },
    "취미": ["독서", "게임"]
}

# json 파일로 저장
with open('c_data.json', 'w', encoding='utf-8') as file:
    # json()메서드
    # data: 저장할 데이터
    # file: 데이터를 담을 파일 객체(json 파일)
    # ensure_ascii=False
    # : json 문자열이 유니코드 의 인코딩 방식을 유지하도록 설정
    # : json의 초기 인코딩은 아스키코드 형식
    # indent=4
    # : 포맷팅 옵션(글자를 가독성 있게 설정)
    # : 각 레벨의 들여쓰기를 4개의 공백으로 설정
    json.dump(data, file, ensure_ascii=False, indent=4)

#! JSON 파일 읽어오기
# json 모듈의 load() 함수 사용
# : JSON 파일의 내용을 파이썬 객체로 변환

with open('c_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)





