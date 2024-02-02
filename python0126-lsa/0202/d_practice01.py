# d_practice01

# 1. [10, 20, 30, 40, 50]의 길이 구하기
length = len([10, 20, 30, 40, 50])
print(length) # 5

# 2. [4, 7, 2, 9, 1, 5]의 최댓값과 최솟값 찾기
numbers = [4, 7, 2, 9, 1, 5]
max_value = max(numbers)
min_value = min(numbers)
print(max_value, min_value) # 9 1

# 3. 리스트 ['banana', 'apple', 'cherry']를 알파벳 순으로 정렬
sorted_list = sorted(['banana', 'apple', 'cherry'])
reverse_sorted_list = sorted(['banana', 'apple', 'cherry'], reverse=True)
print(sorted_list) # ['apple', 'banana', 'cherry']
print(reverse_sorted_list)

# 4. [1, 2, 3, 4, 5]의 모든 요소의 합 구하기
list_sum = sum([1, 2, 3, 4, 5])
print(list_sum) # 15

# 5. 0부터 10까지의 숫자를 포함하는 리스트를 생성
# : range()
# : list() - 연속되는(나열된) 요소를 리스트로 변환
range_list = list(range(0, 11))
print(range_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]