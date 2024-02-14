### 클래스 생성, 생성자, 소멸자 예제 ###

# 게임 구현
# 게임의 캐릭터
# 속성 - name, hp(hit point - 체력), strength
# 기능 - 공격 기능

class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        print(f'캐릭터 {self.name}이 생성되었습니다.')
        print(f'체력은 {self.hp} / 힘은 {self.strength}입니다.')

    def attack(self, other_character):
        print(f'{self.name}이(가) {other_character}을(를) 공격합니다.')
        other_character.hp -= self.strength

    # def __del__(self):
    #     print(f'{self.name}이(가) 게임에서 사라졌습니다.')

    def remove_from_game(self):
        print(f'{self.name}이(가) 게임에서 사라졌습니다.')