### 생성자 & 소멸자 예제 ###

class Service:
    def __init__(self, service):
        self.service = service
        print(f'{self.service} Service가 시작되었습니다.')

    def __del__(self):
        print(f'{self.service} Service가 종료되었습니다.')

s = Service('길 안내')
del s # 인스턴스 삭제 이전에도 소멸자가 실행됨

# 소멸자를 대신해서
# : 해당 기능을 동작하는 메서드를 작성하는 것을 권장