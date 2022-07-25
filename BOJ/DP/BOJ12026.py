# acmicpc.net/problem/12026
n = int(input().rstrip())
road = input().rstrip()
dp = [int(10e8) for _ in range(n+1)]
dp[1] = 1
order = ['B', 'O', 'J']
for d in range(2, n+1):
    idx = 0
    if road[d-1] == 'O':
        idx = 1
    elif road[d-1] == 'J':
        idx = 2
    idx_t = (idx - 1)
    if idx_t == -1:
        idx_t = 2
    val = int(10e8)
    for dd in range(1, d):
        if road[dd-1] == order[idx_t]:
            val = min(val, dp[dd]+((d-dd)**2))
    dp[d] = val
if dp[-1] != int(10e8):
    print(dp[n]-1)
else:
    print(-1)

