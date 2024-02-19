# 파이썬 복습 문제 - p.289
# 다음 지시사항을 읽고 Hybrid 클래스를 구현하세요
# 지시사항
# 1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현하세요.

class Car:
    max_oil = 50  # 최대 주유량

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:  # 0 이하의 주유는 진행하지 않음
            return
        self.oil += oil
        if self.oil > Car.max_oil:  # 주유 후 최대 주유량 초과 상태이면
            self.oil = Car.max_oil  # 현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print('현재 주유상태: {}'.format(self.oil))


# 2. 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
class Hybrid(Car):
    # 최대 배터리 충전량은 30입니다.
    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil)  # 슈퍼 클래스의 생성자를 호출하여 oil 속성을 초기화
        self.battery = battery

    # 배터리를 충전하는 charge() 메서드가 있습니다. 최대 충전량을 초과하도록 충적할 수 없고, 0보다 작은 값으로 충전할 수 없습니다.
    def charge(self, battery):
        if battery <= 0:
            return  # 0이하로 충전하는 것을 방지
        self.battery = battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery  # 현재 배터리 충전량을 최대 충전량으로 설정

    # 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메소드가 있습니다.
    def hybrid_info(self):
        self.car_info()  # 슈퍼 클래스의 car_info 호출
        print('현재 충전상태: {}'.format(self.battery))


# 3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(0, 0)
car.add_oil(55)
car.charge(30)
car.hybrid_info()  # 현재 주유상태: 50 # 현재 충전상태: 30

# Hint: 서브 클래스의 생성자는 반드시 슈퍼 클래스의 생성자를 먼저 호출해야 합니다.
# 서브 클래스에서 슈퍼 클래스의 메소드를 호출하려면 super() 메소드 방식으로 호출할 수 있습니다.