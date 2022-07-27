# https://www.acmicpc.net/problem/5557
n = int(input().rstrip())
nums = list(map(int, input().split()))
nums = [0] + nums
dp = [[0 for _ in range(21)] for _ in range(n)]
dp[1][nums[1]] = 1
for i in range(2, n):
    for j in range(21):
        if dp[i-1][j] != 0:
            if 0 <= j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i-1][j]
                #dp[i][j + nums[i]] += 1
            if 0 <= j - nums[i] <= 20:
                dp[i][j - nums[i]] += dp[i-1][j]
                #dp[i][j - nums[i]] += 1
print(dp[n-1][nums[-1]])