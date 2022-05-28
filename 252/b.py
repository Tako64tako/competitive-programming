import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A,B)
a = np.array(A)
max_Index = [i + 1 for i ,x in enumerate(a) if x == max(a)]
# print(max_Index)
max_value = max(A)
max_index = A.index(max_value) + 1
# print(max_index)
result = "No"
# print(type(max_index))
for _ in B:
    if _ in max_Index:
        result = "Yes"
print(result)