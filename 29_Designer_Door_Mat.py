N, M = map(int, input().split())

for i in range(N):
    if i == N // 2:
        print("WELCOME".center(M, "-"))
    elif i < N // 2:
        print(((2*i + 1) * ".|.").center(M, "-"))
    else:
        print(((2*(N - i - 1) + 1) * ".|.").center(M, "-"))
