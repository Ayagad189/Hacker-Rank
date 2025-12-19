t = int(input())

for _ in range(t):
    a_n = int(input())
    a = set(map(int, input().split()))
    b_n = int(input())
    b = set(map(int, input().split()))
    
    print(a.issubset(b))
