# 클래스 예제 #

# 사용자로부터 온전한 수식을 입력받고,
# 입력된 수식의 결과를 출력하는 Calculator 클래스

class Calculator:

    def input_expr(self):
        # 수식을 입력받아서 인스턴스 변수인 expr에 저장
        expr = input('수식을 입력하세요 >> ')
        self.expr = expr # 우항의 expr는 10번 째 줄의 입력값

    def calculate(self):
        # eval(): 문자열로 된 수식 자체를 계산할 수 있는 함수
        return eval(self.expr)

# Calculator 클래스를 기반으로 calc 인스턴스 생성
calc = Calculator()

# 사용자가 수식을 입력할 수 있는 콘솔창 생성
calc.input_expr()

# calculate() 메서드를 호출하면 수식 결과가 반환
result = calc.calculate()
print(f'수식 결과는 {result}입니다.')

# self
# : 클래스 내부에서 호출한 객체를 찾기 위해 해당 함수를 호출한
#   객체 그 자체를 가리킴

# 클래스 생성 예제 #
# 자동차 클래스: Car
# - 각 자동차의 브랜드, 모델, 연료 타입, 색상 (인스턴스 변수)
# - 자동차가 수행할 수 있는 기본 동작
#   : 운전하기, 가속하기, 정지하기 (인스턴스 메서드)

class Car:
    # 인스턴스 변수 - 명시적으로 정의
    brand = ''
    model = ''
    fuel_type = ''
    color = ''

    # 인스턴스 메서드
    def set_datails(self, brand, model, fuel_type, color):
        # self.brand가 39번 째 줄의 brand 변수를 가리킴
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.color = color

    def drive(self):
        print(f'{self.brand} {self.model} is driving')

    def accelerate(self):
        print(f'{self.brand} {self.model} is accelrating')

    def stop(self):
        print('운행이 종료되었습니다.')

# 자동차 인스턴스 생성 / 세부 정보 설정
car1 = Car()
car1.set_datails('Hyundai', 'Sonata', 'Gasoline', 'Blue')

car2 = Car()
car2.set_datails('Tesla', 'Model S', 'Electric', 'White')

# car1 동작 시연
car1.drive()
car1.accelerate()
car1.stop()

# car2 동작 시연
car2.drive()
car2.accelerate()
car2.stop()