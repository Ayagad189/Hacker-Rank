import numpy as np

n, m = map(int, input().split())
myarray = []

for _ in range(n):
    row = list(map(int, input().split()))
    myarray.append(row)

my_array = np.array(myarray)
row_mins = np.min(my_array, axis=1)
print(np.max(row_mins))
