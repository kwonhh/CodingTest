# https://www.acmicpc.net/problem/11726

N = int(input().rstrip())

if N < 3:
    print(N)
else:
    p = [0 for _ in range(N+1)]
    p[1] = 1
    p[2] = 2

    for i in range(3, N+1):
        p[i] = p[i-1] + p[i-2]
    print(p[N]%10007)