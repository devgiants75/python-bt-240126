# csv 파일을 다루기 위한 csv 모듈 임포트
import csv
# 시각화를 위한 matplotlib.pyplot 모듈을 plt로 임포트
import matplotlib.pyplot as plt

# 날씨 데이터를 관리하는 클래스 정의
class WeatherDataManager:
    def __init__(self, filename):
        # 객체 생성 시 파일 이름을 인스턴스 변수로 저장
        self.filename = filename

    def create_data(self, city_name, date, max_temp, min_temp, rainfall):
        # csv파일에 새로운 날씨 데이터를 추가하는 메서드
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # 입력받은 데이터를 csv 파일에 한 행으로 추가
            writer.writerow([city_name, date, max_temp, min_temp, rainfall])

    def read_data(self):
        # csv 파일의 모든 날씨 데이터를 출력하는 메서드
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # 파일의 각 행을 출력
                print(row)

    def update_data(self, city_name, new_data):
        # 특정 도시와 날짜의 날씨 데이터를 수정하는 메서드
        # ._load_data(): 파일에서 데이터를 로드
        data = self._load_data()
        for row in data:
            # 한 행이 배열로 구성
            # 배열 내에는 도시명0, 날짜1, 최고기온, 최저기온, 강수량
            if row[0] == city_name and row[1] == data:
                # 조건에 맞는 행의 데이터를 업데이트
                row[2:] = new_data
            # 수정된 데이터를 파일에 다시 저장
            self._save_data(data)

    def delete_data(self, city_name, date):
        # 특정 도시와 날짜의 날씨 데이터를 삭제하는 메서드
        data = self._load_data() # 파일에서 데이터를 로드
        # 조건에 맞지 않는 행만 새로운 데이터 목록을 생성
        # 데이터를 삭제할 때
        # : 해당 데이터의 조건과 일치하는 데이터를 제외한 목록을 생성하여
        # : 새로운 데이터로 생성하여 저장
        # >> 삭제의 효과를 나타냄
        data = [
            row for row in data
            if not (row[0] == city_name and row[1] == date)
        ]
        # 삭제하고자 하는 데이터를 제외한 데이터만 새롭게 저장
        self._save_data(data)

    def _load_data(self):
        # csv 파일에서 날씨 데이터를 로드하는 내부 메서드
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            # 파일의 각 행을 리스트로 반환
            return [row for row in reader]

    def _save_data(self, data):
        # 날씨 데이터를 csv 파일에 저장하는 내부 메서드
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # 주어진 데이터를 파일에 쓰기
            writer.writerows(data)

#! 날씨 데이터를 시각화하는 클래스 정의
class WeatherVisualization:
    @staticmethod
    # 정적 메서드로, 날씨 데이터를 선 그래프로 시각화
    # data 파라미터는 날씨 정보가 담긴 2차원 리스트
    def visualize(data):
        # 데이터에서 유일한 도시 이름들을 추출하여 집합으로 저장
        city_names = set(row[0] for row in data)

        # 각 도시에 대한 데이터를 순회
        for city in city_names:
            # 해당 도시의 날씨 데이터만 추출
            city_data = [row for row in data if row[0] == city]
            # 해당 도시의 날씨 데이터에서 날짜 정보를 추출
            dates = [row[1] for row in city_data]
            # 해당 도시의 날씨 데이터에서 최고 기온 정보를 추출(숫자로 변환)
            max_temps = [float(row[2]) for row in city_data]
            # 해당 도시의 날씨 데이터에서 최저 기온 정보를 추출(숫자로 변환)
            min_temps = [float(row[3]) for row in city_data]

            # 해당 도시의 날짜와 최고 & 최저 기온을 사용하여 선 그래프를 생성
            plt.plot(dates, max_temps, label=f'{city} Max Temp')
            plt.plot(dates, min_temps, label=f'{city} Min Temp')


        plt.xlabel('Date') # x축 레이블 추가
        plt.ylabel('Temperature') # y축 레이블 추가
        plt.legend() # 범례 추가
        plt.show() # 그래프를 화면에 표시

#! main 함수 작성
# : 실행 함수
def main():
    # 날씨 데이터를 저장할 csv 파일의 이름을 설정
    filename = 'weater_data.csv'

    # WeatherDataManager 클래스의 인스턴스를 생성
    # , 파일 이름을 매개변수로 전달
    weather_manager = WeatherDataManager(filename)

    # 무한 루프를 통해 사용자로부터 계속해서 명령을 받기
    while True:
        print('Enter command')
        command = input('create/read/update/delete/visualize/exit : ')

        if command == 'create':
            # 'create'명령을 받으면, 새로운 날씨 데이터를 생성
            # 사용자로부터 필요한 정보를 입력받기
            city_name = input('Enter City Name: ')
            date = input('Enter Date (YYYY-MM-DD): ')
            max_temp = input('Enter Max Temperature: ')
            min_temp = input('Enter Min Temperature: ')
            rainfall = input('Enter Rainfall: ')

            # 입력받은 정보를 이용해 새로운 날씨 데이터를 csv 파일에 저장
            weather_manager.create_data(city_name, date, max_temp, min_temp, rainfall)

        elif command == 'read':
            # 'read'명령을 받으면, 저장된 날씨 데이터를 읽어와 화면에 출력
            weather_manager.read_data()
        elif command == 'update':
            city_name = input('Enter city name')
            date = input('Enter date (YYYY-MM-DD)')
            # 18,15,0
            new_date = input('Enter new max, min, rainfall data(seperated by comma)').split(',')

            # 입력받은 데이터로 특정 도시와 날짜의 날씨 데이터를 수정
            weather_manager.update_data(city_name, date, new_date)

        elif command == 'delete':
            city_name = input('Enter city name')
            date = input('Enter date (YYYY-MM-DD)')

            # 해당하는 날씨 데이터를 삭제
            weather_manager.delete_data(city_name, date)

        elif command == 'visualize':
            # csv 파일에서 날씨 데이터를 로드
            data = weather_manager._load_data()

            # 로드된 날씨 데이터를 시각화
            WeatherVisualization.visualize(data)

        elif command == 'exit':
            break # 프로그램을 종료

        else: # 입력된 명령어가 유효하지 않은 경우 오류 메시지를 출력
            print('Invalid Command')

main()

