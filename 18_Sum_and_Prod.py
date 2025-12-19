import numpy as np

n, m = map(int, input().split())
myarray = []

for _ in range(n):
    row = list(map(int, input().split()))
    myarray.append(row)

my_array = np.array(myarray)
s = np.sum(my_array, axis=0)
print(np.prod(s))
