# https://www.acmicpc.net/problem/2748

N = int(input().rstrip())
p = [0 for _ in range(N+1)]
p[1] = 1

for i in range(2, N+1):
    p[i] = p[i-1] + p[i-2]

print(p[N])