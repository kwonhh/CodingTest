# https://www.acmicpc.net/problem/1495

songs, startv, maxv = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0 for _ in range(maxv + 1)] for _ in range(songs+1)]

dp[0][startv] = 1
for i in range(1, songs+1):
    for ii in range(maxv+1):
        if dp[i-1][ii] == 1:
            if ii + v[i-1] <= maxv:
                dp[i][ii + v[i-1]] = 1
            if ii - v[i-1] >= 0:
                dp[i][ii - v[i-1]] = 1
ans = -1
for d in range(maxv, -1, -1):
    if dp[songs][d] == 1:
        ans = d
        break
print(ans)