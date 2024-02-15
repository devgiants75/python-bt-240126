### 파이썬 클래스 복습 문제 ###

# 교재: p.288
# 분식점 가게 매출을 구할 수 있는 Shop 클래스 구현

# 1. Shop 클래스
# 전체 매출액을 저장: total 클래스 변수
# 메뉴 리스트 딕셔너리로 저장: menu_list 클래스 변수
class Shop:
    #! 클래스 변수
    total = 0 # 가게 총 매출
    # 가게 메뉴 리스트를 딕셔너리 형식으로 정리
    menu_list = [{'떡볶이': 3000}, {'어묵': 700}, {'튀김': 500}, {'김밥': 2000}]

    #! 클래스 메서드
    @classmethod
    def sales(cls, menu, amount):
        # for in 반복문
        # 메뉴 리스트에서 메뉴를 가져와
        # 해당 메뉴(menu)가 메뉴 리스트에 존재하는지 확인
        for item in cls.menu_list:
            if menu in item:
                # 인스턴스의 총 합계를 더하기할당 연산을 통해 구현
                # 메뉴 가격과 판매량을 곱한 뒤 전체 매출액에 더함
                cls.total += item[menu] * amount
                return
        # 해당 메뉴가 없을 경우
        print(f'{menu}는 저희 가게 메뉴에 없습니다.')

# 매출이 생기면 메뉴와 판매량을 작성
Shop.sales('떡볶이', 1) # 3000
Shop.sales('튀김', 5) # 2500
Shop.sales('김밥', 2) # 4000
Shop.sales('라면', 2)

# 총 매출
print(f'총 매출은 {Shop.total}') # 총 매출은 9500


### 파이썬 클래스 상속 복습 문제 ###

# 차량 관리 시스템
# Vehicle 클래스 (부모)
# Car 클래스 (자식)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

    def drive(self):
        print(f'{self.description()} is now driving')

class Car(Vehicle):
    def __init__(self, make, model, year, trunk_size):
        super().__init__(make, model, year)
        self.trunk_size = trunk_size

    def open_trunk(self):
        print(f'{self.description()} / Trunk size: {self.trunk_size}')

# 운송수단 인스턴스 생성 및 사용
vehicle = Vehicle('Hundai', 'sonata', 2021)
print(vehicle.description())
vehicle.drive()

# 승용차 인스턴스 생성 및 사용
car = Car('Toyota', 'Corolla', 2020, trunk_size=450)
print(car.description()) # 부모 클래스의 메서드
car.open_trunk()