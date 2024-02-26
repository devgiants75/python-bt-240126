#! Person 클래스 생성
# : 각 개인의 정보를 저장할 클래스
# : 이름, 전화번호, 주소 정보를 저장

import sys # 파이썬 내부 라이브러리

class Person:
    # 생성자를 사용하여 해당 정보를 전달
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    # info(): 추가로 저장된 정보를 출력하는 메서드
    def info(self):
        print(f'{self.name}, {self.phone}, {self.address}')

#! AddressBook 클래스 생성
# : 주소록 프로젝트의 모든 기능을 구현하는 클래스
# : Person클래스의 객체를 여러 개 저장할 수 있는 address_list 배열을 포함

class AddressBook:
    # 생성자
    # : csv 파일을 읽어서 address_list 리스트에 저장
    # : 리스트 생성 후 csv 파일을 읽어오는 file_reader()메서드를 호출
    def __init__(self):
        self.address_list = []
        self.file_reader()

    # csv 파일 읽기
    # : csv 파일의 정보를 address_list에 저장하는 메서드
    def file_reader(self):
        try: # csv 파일이 없으면 예외 발생
            file = open('addressBook.csv', 'rt', encoding='utf-8', errors='replace')
        except: # csv 파일이 없을 때
            print('addressBook 파일이 없습니다.')
        else: # csv 파일이 있을 때
            for buffer in file:
                if buffer.strip():  # 공백 라인 건너뛰기
                    name, phone, address = buffer.strip().split(',')
                    self.address_list.append(Person(name, phone, address))
            print('addressBook.csv 파일을 로드했습니다.')
            file.close()

    # csv 파일 생성
    # : address_list의 모든 데이터를 사용하여 csv 파일을 생성
    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt', encoding='utf-8')
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write(f'{person.name},{person.phone},{person.address}\n')
            file.close()

    # 수행 메뉴 소개 및 입력
    # : 프로그램의 동작을 안내하는 출력문으로 구성
    # : 어떤 동작을 수행할 것인지 사용자로부터 입력받아서 그 값을 반환
    @staticmethod
    def menu():
        print('-' * 30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        print('-' * 30)
        choice = int(input('수행할 작업을 숫자로 입력하세요 : '))
        return choice

    # 프로그램 종료
    # : sys 모듈의 exit() 메서드를 호출하여 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()

    # 프로그램 실행
    # : 사용자로 부터 입력받은 값으로 작업할 해당 메서드를 호출
    def run(self):
        while True:
            # menu() 메서드는 정적 메서드 - 클래스명으로 호출
            choice = AddressBook.menu()
            if choice == 0: self.exit()
            elif choice == 1: self.insert() # 신규 주소록 등록
            elif choice == 2: self.delete() # 기존 주소록 삭제
            elif choice == 3: self.update() # 기존 주소록 수정
            elif choice == 4: self.search() # 주소록 검색
            elif choice == 5: self.print_all() # 전체 주소록 출력
            else: print('없는 번호입니다. 확인 후 다시 입력해주세요.')

    # insert()
    # : 사용자로부터 새로 등록할 이름, 전화번호, 주소를 입력받고
    # : Person 객체를 생성하여 해당 객체를 address_list에 저장
    def insert(self):
        print('== 신규 주소록 생성 ==')
        name = input('등록할 이름 입력: ')
        phone = input('등록할 전화번호 입력: ')
        address = input('등록할 주소 입력: ')

        if name and phone and address: # 모두 입력되었을 경우
            self.address_list.append(Person(name, phone, address)) # 삽입
            # 변경된 address_list의 내용으로 csv 파일을 새로 생성
            self.file_generator()
            print('신규 주소록이 정상적으로 생성되었습니다.')
        else:
            # 누락된 입력이 하나라도 있는 경우 - 삽입 실패
            print('입력값이 부족하여 주소록이 생성되지 않았습니다.')

    # delete()
    # : 사용자로부터 삭제하고자 하는 데이터의 이름을 입력받아
    # : address_list에서 제거
    def delete(self):
        print('== 기존 주소록 삭제 ==')
        name = input('삭제할 이름 입력: ')
        if not name:
            print('입력된 이름이 주소록에 없습니다. 삭제할 수 없습니다.')
            return
        deleted = False
        # enumerate: 파이썬 내장 함수
        # - 순회가능한 iterable의 각 원소와 그 원소의 인덱스를 튜플로 묶어서 반환
        for i, person in enumerate(self.address_list):
            if name == person.name:
                print(f'검색된 전화번호가 {person.phone}입니다.')
                # 사용자의 입력을 받은 후 대문자로 변환
                if input('삭제할까요? (Y/N) : ').upper() != 'Y':
                    continue # for문으로 되돌아가 다음 사람을 검색
                del self.address_list[i]  # 해당 인덱스의 요소를 삭제
                deleted = True
                print(f'{name}의 정보를 삭제했습니다.')
                self.file_generator()
                break
        if not deleted:
            print(f'{name}의 정보가 삭제되지 않았습니다.')

    # update()
    # : 사용자로부터 수정할 사용자 정보를 입력받아서
    # : address_list에서 사용자를 찾아와 정보를 수정
    def update(self):
        print('=== 기존 주소록 수정 ===')
        name = input('수정할 이름을 입력 : ')
        if not name:
            print('입력된 이름이 없어 수정을 취소합니다.')
            return
        updated = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                if name == person.name:
                    print(f'검색된 전화번호가 "{person.phone}"입니다.')
                    # 수정 여부를 묻는 메시지를 먼저 출력하고, 대문자로 변환된 입력을 받음
                    confirm = input('수정할까요? (Y/N) : ').upper()
                    if confirm != 'Y':
                        continue  # 사용자가 'Y'가 아니면 다음 사람을 검색

                    new_phone = input('변경할 전화번호 입력 : ')
                    if new_phone:  # 입력이 있는 경우
                        person.phone = new_phone  # 입력된 내용으로 변경

                    new_address = input('변경할 주소 입력 : ')
                    if new_address:
                        person.address = new_address

                    updated = True
                    print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요.')
                    person.info()  # 수정된 정보 출력
                    self.file_generator()  # 파일 업데이트
                    break
        if not updated:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))

    # search()
    # : 특정 주소록 정보를 검색해서 출력하는 메서드
    # : 사용자로부터 이름을 입력받아서 동일한 정보를 찾아 모두 출력
    # - 같은 이름이 2명 이상 포함(검색된 데이터 모두를 출력)
    # - 검색된 사람이 없으면 '{}의 정보가 없습니다.'라는 메시지를 출력
    def search(self):
        print('=== 주소록 검색 ===')
        name = input('찾을 이름을 입력 : ')
        if not name:
            print('입력된 이름이 없어 검색을 취소합니다.')
            return
        exist = False # 검색되었는 유무를 판단하는 플래그 변수
        for person in self.address_list:
            if name == person.name:
                person.info()
                exist = True
        if not exist:
            print('{}의 정보가 없습니다.'.format(name))

    # print_all()
    # : 전체 주소록 정보를 출력하는 메서드
    def print_all(self):
        print('== 전체 연락처 출력 ==')
        for person in self.address_list:
            person.info()
        print(f'총 {len(self.address_list)}개의 주소록이 있습니다.')

my_app = AddressBook()
my_app.run()