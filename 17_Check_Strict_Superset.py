a = set(map(int, input().split()))
n = int(input())
count = 0

for _ in range(n):
    s = set(map(int, input().split()))
    if a.issuperset(s):
        count += 1

print(count == n)
