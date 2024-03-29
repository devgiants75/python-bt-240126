# 파이썬 복습 문제 - p.289

# 다음 지시사항을 읽고 Hybrid 클래스를 구현

# 지시사항
# : 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현

# 1. 슈퍼 클래스 Car 구현
# Car 클래스는 최대 주유량(max_oil)을 클래스 변수로 가지며, 이 값은 50으로 설정

# __init__ 메서드를 통해 초기 주유량(oil)을 설정

# add_oil 메서드를 통해 주유를 추가할 수 있으며
# , 주유량이 0 이하이거나 최대 주유량을 초과하는 경우의 처리가 필요

# car_info 메서드를 통해 현재 주유 상태를 출력

# 2. 서브 클래스 Hybrid 구현
# Hybrid 클래스는 Car 클래스를 상속

# 최대 배터리 충전량(max_battery)을 클래스 변수로 가지며, 이 값은 30으로 설정

# __init__ 메서드를 통해 초기 주유량(oil)과 배터리 충전량(battery)을 설정

# charge 메서드를 통해 배터리를 충전할 수 있으며
# , 충전량이 0 이하이거나 최대 충전량을 초과하는 경우의 처리가 필요

# hybrid_info 메서드를 통해 현재 주유량과 충전량을 모두 확인

#! 동작 확인
# Hybrid 인스턴스를 생성하고, 주유와 충전을 진행한 후
# , 현재 상태를 출력하여 모든 기능이 올바르게 동작하는지 확인