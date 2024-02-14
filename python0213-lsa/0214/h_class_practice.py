### 클래스 생성 예제 ###

# 공상 과학 테마 게임 #

# 우주선을 조종, 행성 탐험, 우주 해적과의 전투
# 우주선 클래스(Spaceship)
# 속성 - 이름(name), 에너지(energy), 무기력(weapon_power)
# 기능 - 행성 탐험, 에너지 충전, 우주 해적과의 전투

class Spaceship:
    def __init__(self, name, energy, weapon_power):
        self.name = name
        self.energy = energy
        self.weapon_power = weapon_power
        print(f'우주선 {self.name}이(가) 발진 준비 완료')
        print(f'에너지는 {self.energy} / 무기력 {self.weapon_power}')

    def explore_planet(self):
        if self.energy > 10:
            print(f'{self.name}이(가) 새로운 행성을 탐험합니다.')
            self.energy -= 10
        else:
            print(f'{self.name}의 에너지가 부족하여 탐험을 계속할 수 없습니다.')
            print('에너지를 충전하세요')

    def recharge(self, amount):
        self.energy += amount
        print(f'{self.name}의 에너지가 {amount}만큼 충전되었습니다.')
        print(f'현재 에너지는 {self.energy}입니다.')

    def battle(self, enemy_power):
        if self.energy > 20 and self.weapon_power > enemy_power:
            print(f'{self.name}이(가) 우주 해적과의 전투에서 승리하였습니다.')
            self.energy -= 20
        else:
            print(f'{self.name}이(가) 전투에서 패배했습니다.')

    def destroy_ship(self):
        print(f'우주선 {self.name}이(가) 파괴되었습니다. 게임에서 제거됩니다.')

seungah = Spaceship('승아호', 100, 80)
dokyung = Spaceship('도경호', 120, 40)

seungah.explore_planet()
seungah.recharge(50)
seungah.battle(dokyung.weapon_power)
dokyung.destroy_ship()