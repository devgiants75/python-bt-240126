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