# 리스트 메서드 #

# 1. append()
# : 리스트의 끝에 새로운 요소를 추가
# : 리스트.append(추가할 요소)
animals = ['cat', 'dog']
animals.append('elephant')
print(animals) # ['cat', 'dog', 'elephant']

# 2. extend()
# : 리스트의 끝에 다른 리스트를 연결하여 확장
# : 리스트.extend(추가할 리스트)
animals = ['cat', 'dog']
more_animals = ['tiger', 'lion']
animals.extend(more_animals)
print(animals) # ['cat', 'dog', 'tiger', 'lion']

# 3. insert()
# : 리스트의 특정 위치(인덱스)에 새로운 요소를 삽입
# : 리스트.insert(특정위치, 새로운요소)
animals = ['cat', 'dog']
animals.insert(1, 'elephant')
print(animals) # ['cat', 'elephant', 'dog']

# 4. clear()
# : 리스트의 모든 요소를 제거, 빈 리스트를 생성
animals = ['cat', 'dog']
animals.clear()
print(animals) # []

# 5. pop()
# : 리스트의 특정 위치의 요소를 제거, 해당 요소를 반환
# 리스트.pop(제거할요소의위치)
animals = ['cat', 'dog', 'tiger']
removed_animal = animals.pop(1)
print(removed_animal) # dog
print(animals) # ['cat', 'tiger']

# 6. remove()
# : 리스트에서 첫 번째로 나타나는 특정 값을 제거
# 리스트.remove(제거할요소)
animals = ['cat', 'dog', 'tiger', 'dog']
animals.remove('dog')
print(animals) # ['cat', 'tiger', 'dog']
