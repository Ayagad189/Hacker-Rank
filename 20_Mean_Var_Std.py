import numpy as np

n, m = map(int, input().split())
myarray = []

for _ in range(n):
    row = list(map(int, input().split()))
    myarray.append(row)

my_array = np.array(myarray)

print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(round(np.std(my_array), 11))
