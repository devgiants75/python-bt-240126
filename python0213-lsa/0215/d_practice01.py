# 클래스 변수 / 클래스 메서드 / 정적 메서드 #

# 교재: p.282
# 가방을 만들 때마다, 현재 만들어진 가방이 몇 개인지 계산하는 Bag 클래스

class Bag:

    count = 0

    def __init__(self):
        # 생성자가 호출될 때마다 count가 1씩 증가
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1 # 가방 판매 시 count가 1씩 감소

    @classmethod
    def remain_bag(cls):
        return cls.count # 남아있는 가방의 개수

print('현재 가방: {}'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('현재 가방: {}'.format(Bag.remain_bag()))

# 전구 클래스 #
# 1. 전구가 생성될 때마다 전체 전구의 수를 추적 - 클래스 메서드
# 2. 전구가 판매 or 폐기될 때 수를 감소 - 클래스 메서드
# 3. 전구의 수명이 얼마나 남았는지 계산 - 정적 메서드

class LightBulb:
    total_count = 0

    def __init__(self):
        LightBulb.total_count += 1

    @classmethod
    def sell_bulb(cls):
        if cls.total_count > 0:
            cls.total_count -= 1
        else:
            print('판매할 전구가 없습니다.')

    @classmethod
    def current_stock(cls):
        return cls.total_count

    # 전구의 수명 계산
    # : 전구의 수명을 시간 단위로 받아, 평균적으로 몇 년 지속될지 계산
    @staticmethod
    def calculate_lifttime(hours):
        years = hours / (24 * 365)
        return years

# 클래스 사용
print('---전구 예제---')
print(f'초기 전구: {LightBulb.current_stock()}개')

# range()로 5개의 LigthBulb 인스턴스를 생성
new_bulbs = [LightBulb() for _ in range(5)]

print(f'전구 생성 후: {LightBulb.current_stock()}개')

# 전구 판매
LightBulb.sell_bulb()
LightBulb.sell_bulb()

print(f'전구 판매 후: {LightBulb.current_stock()}개')

lifetime = LightBulb.calculate_lifttime(10000)
print(f'전구의 수명: {lifetime:.2f}년')