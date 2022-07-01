# https://www.acmicpc.net/problem/2579

N = int(input().rstrip())
stair = [0 for _ in range(N+1)]
for i in range(1, N+1):
    stair[i] = int(input().rstrip())

p = [[0, 0, 0] for _ in range(N+1)]
p[1][0] = stair[1]
p[1][2] = 1
for i in range(2, N+1):
    p[i][1] = max(p[i-2][:2]) + stair[i]

    if p[i-1][0] < p[i-1][1] or (p[i-2][2] == 1 and p[i-1][2] == 1):
        p[i][0] = p[i-1][1] + stair[i]
        p[i-1][2] = 1
        p[i][2] = 1
    else:
        p[i][0] = p[i-1][0] + stair[i]
        p[i][2] = 1

print(max(p[N][:2]))