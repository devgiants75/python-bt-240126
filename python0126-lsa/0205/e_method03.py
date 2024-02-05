# 파이썬 메서드 - 세트
# 순서X, 변경O, 중복X
# {} 중괄호 사용

# 1. 교집합: intersection()
fruits1 = {'apple', 'banana'}
fruits2 = {'banana', 'orange'}

result = fruits1.intersection(fruits2)
print(result) # {'banana'}

# 2. 합집합: union()
result = fruits1.union(fruits2)
print(result) # {'apple', 'orange', 'banana'}
# >> set 자료형은 중복을 허용하지 않기 때문에
#    동일한 값은 하나의 값만 남김

# 3. 차집합: difference
result1 = fruits1.difference(fruits2)
result2 = fruits2.difference(fruits1)
print(result1) # {'apple'}
print(result2) # {'orange'}