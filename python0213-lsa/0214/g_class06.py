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

# Character 클래스를 사용한 객체 생성
Naymar = Character('Naymar', 300, 50)
Son = Character('Son', 400, 150)

# 객체의 메서드의 인자로 또 다른 객체를 전달 가능
Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다')

Naymar.attack(Son)
print(f'손흥민의 남은 체력은 {Son.hp}입니다.')

Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다')

# 캐릭터의 체력이 0이 되는 경우 제거
if Naymar.hp <= 0:
    Naymar.remove_from_game()
    del Naymar