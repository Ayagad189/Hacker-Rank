N = int(input())
s = set(map(int, input().split()))
M = int(input())

for _ in range(M):
    command = input().split()
    s_n = set(map(int, input().split()))

    if command[0] == "update":
        s.update(s_n)
    elif command[0] == "intersection_update":
        s.intersection_update(s_n)
    elif command[0] == "difference_update":
        s.difference_update(s_n)
    elif command[0] == "symmetric_difference_update":
        s.symmetric_difference_update(s_n)

print(sum(s))
