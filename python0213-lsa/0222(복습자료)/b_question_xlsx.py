# 문제 1: 엑셀 파일 생성하기
# 데이터프레임을 생성하고 이를 엑셀 파일로 저장
#
# 다음 데이터를 포함하는 pandas DataFrame을 생성
# 이름: ['John Doe', 'Jane Smith', 'Emily Davis']
# 나이: [28, 34, 42]
# 성별: ['Male', 'Female', 'Female']
# 직업: ['Software Engineer', 'Data Scientist', 'Project Manager']
# 이 DataFrame을 'employees.xlsx' 파일로 저장
# 저장된 엑셀 파일을 pandas를 사용하여 불러오고, 전체 데이터를 출력

#---------------------------------------------#
# 문제 2: 엑셀 파일 조회하기
# 저장된 엑셀 파일 'employees.xlsx'에서 데이터를 조회
#
# 'employees.xlsx' 파일을 불러온 후, 나이가 30 이상인 사람들만 필터링하여 출력
# '성별'이 'Female'인 모든 직원의 이름과 직업을 출력

#---------------------------------------------#
# 문제 3: 엑셀 파일 변경하기
# 엑셀 파일에 새로운 데이터를 추가하고 변경
#
# 'employees.xlsx' 파일에 다음 데이터를 추가
# 이름: 'Lucas Brown', 나이: 30, 성별: 'Male', 직업: 'Marketing Manager'
# 'John Doe'의 직업을 'Senior Software Engineer'로 변경
# 변경된 DataFrame을 'updated_employees.xlsx'로 저장

#---------------------------------------------#
# 문제 4: 엑셀 파일에서 데이터 삭제하기
# 엑셀 파일에서 특정 데이터를 삭제
#
# 'updated_employees.xlsx' 파일에서 'Emily Davis'의 데이터를 삭제
# 결과를 'modified_employees.xlsx'로 저장

#---------------------------------------------#
#문제 5: 엑셀 파일 업데이트하기
# 엑셀 파일을 업데이트하여 새로운 시트에 데이터를 추가
#
# 'modified_employees.xlsx' 파일을 열고, 새로운 시트 'Departments'를 추가
# 'Departments' 시트에 다음 데이터를 포함하는 DataFrame을 추가
# 부서: ['Engineering', 'Data Science', 'Marketing']
# 부서장: ['John Doe', 'Jane Smith', 'Lucas Brown']
# 파일을 저장하고 변경 사항을 확인