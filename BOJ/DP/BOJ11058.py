# https://www.acmicpc.net/problem/11058

N = int(input().rstrip())
dp = [0 for _ in range(N+1)]
for n in range(1, N+1):
    if n <= 6:
        dp[n] = n
        continue
    dp[n] = max(dp[n - 3] * 2, dp[n - 4] * 3, dp[n - 5] * 4, dp[n-6]*5, dp[n - 1] + 1)
print(dp[-1])