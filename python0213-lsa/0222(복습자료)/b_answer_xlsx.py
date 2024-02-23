import pandas as pd

# 문제 1: 엑셀 파일 생성하기
# 데이터프레임 생성
df = pd.DataFrame({
    '이름': ['John Doe', 'Jane Smith', 'Emily Davis'],
    '나이': [28, 34, 42],
    '성별': ['Male', 'Female', 'Female'],
    '직업': ['Software Engineer', 'Data Scientist', 'Project Manager']
})
# 엑셀 파일로 저장
df.to_excel('employees.xlsx', index=False)

# 문제 1-3: 저장된 엑셀 파일 불러오기 및 데이터 출력
df_loaded = pd.read_excel('employees.xlsx')
print("문제 1-3: 저장된 엑셀 파일 데이터")
print(df_loaded)

# 문제 2: 엑셀 파일 조회하기
# 나이가 30 이상인 사람들 필터링
df_age_over_30 = df_loaded[df_loaded['나이'] >= 30]
print("\n나이가 30 이상인 사람들:")
print(df_age_over_30)

# 성별이 'Female'인 모든 직원 조회
df_female = df_loaded[df_loaded['성별'] == 'Female'][['이름', '직업']]
print("\n성별이 'Female'인 모든 직원의 이름과 직업:")
print(df_female)

# 문제 3: 엑셀 파일 변경하기
# 새로운 데이터 추가
new_data = pd.DataFrame([{'이름': 'Lucas Brown', '나이': 30, '성별': 'Male', '직업': 'Marketing Manager'}])
df_loaded = pd.concat([df_loaded, new_data], ignore_index=True)
# 'John Doe'의 직업 변경
df_loaded.loc[df_loaded['이름'] == 'John Doe', '직업'] = 'Senior Software Engineer'
# 변경된 데이터프레임 저장
df_loaded.to_excel('updated_employees.xlsx', index=False)

# 문제 4: 엑셀 파일에서 데이터 삭제하기
# 'Emily Davis'의 데이터 삭제
df_modified = df_loaded[df_loaded['이름'] != 'Emily Davis']
# 결과 저장
df_modified.to_excel('modified_employees.xlsx', index=False)

# 문제 5: 엑셀 파일 업데이트하기
# 새로운 시트에 데이터 추가하기
with pd.ExcelWriter('modified_employees.xlsx', engine='openpyxl', mode='a') as writer:
    df_departments = pd.DataFrame({
        '부서': ['Engineering', 'Data Science', 'Marketing'],
        '부서장': ['John Doe', 'Jane Smith', 'Lucas Brown']
    })
    df_departments.to_excel(writer, sheet_name='Departments', index=False)

# 파일 경로 출력
print("\n엑셀 파일이 생성 및 수정되었습니다. 파일 경로:")
print("employees.xlsx")
print("updated_employees.xlsx")
print("modified_employees.xlsx")