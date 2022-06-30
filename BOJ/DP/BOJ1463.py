# https://www.acmicpc.net/problem/1463

N = int(input().rstrip())
p = [0 for _ in range(1+N)]

for i in range(2, N+1):
    p[i] = p[i-1] + 1

    if i % 2 == 0:
        p[i] = min(p[i], p[i // 2] + 1)
    if i % 3 == 0:
        p[i] = min(p[i], p[i // 3] + 1)

print(p[N])
