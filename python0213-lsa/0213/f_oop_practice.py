### 객체 지향 프로그래밍 도입 필요성 ###

# 학생 정보를 전달하는 student_info() 함수
# 이름, 학년, 반, 전화번호, 주소, 성적

def student_info(name, grade, class_number, phone_number, address, score):
    # 학생 정보를 print()으로 출력
    print(name)
    print(grade)
    print(class_number)
    print(phone_number)
    print(address)
    print(score)

# student_info()함수를 사용하여 학생1 생성
name1 = "이승아"
grade1 = 3
class_number1 = 2
phone_number1 = "010-1234-1234"
address1 = "부산시 연제구"
scord1 = 90

student_info(name1, grade1, class_number1, phone_number1, address1, scord1)

# student_info()함수를 사용하여 학생2 생성
name2 = "이도경"
grade2 = 1
class_number2 = 12
phone_number2 = "010-5678-5678"
address2 = "부산시 부산진구"
scord2 = 95

student_info(name2, grade2, class_number2, phone_number2, address2, scord2)

# 클래스를 이용한 학생 관리 #
class Student:
    def __init__(self, name, grade, class_number):
        self.name = name
        self.grade = grade
        self.class_number = class_number

    def print_info(self):
        print(f'Name: {self.name}, Grade: {self.grade}, ClassNumber: {self.class_number}')

student1 = Student('이승아', 3, 2)
student2 = Student('이도경', 1, 12)

student1.print_info()
student2.print_info()

# 절차 지향 #

# 1. 변수 선언
number_list = [1, 2, 3, 4, 5]

# 2. 함수 정의
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 함수 호출
total_sum = sum_numbers(number_list)
print("Total Sum: ", total_sum)

# 객체 지향 #

# 1. 클래스 정의
class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_numbers(self):
        return sum(self.numbers) # 리스트의 내장 함수

# 2. 객체 생성
my_number_list = NumberList([1, 2, 3, 4, 5])

# 3. 메서드 호출
print("Total Sum: ", my_number_list.sum_numbers())