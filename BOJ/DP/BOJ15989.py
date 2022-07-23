# https://www.acmicpc.net/problem/15989
def solution(n):
    for nn in range(tmp+1, n+1):
        if nn == 1:
            dp[1][1] = 1
            continue
        if nn == 2:
            dp[2][1] = 1
            dp[2][2] = 1
            continue
        if nn == 3:
            dp[3][1] = 1
            dp[3][2] = 1
            dp[3][3] = 1
            continue
        dp[nn][1] = dp[nn-1][1]
        dp[nn][2] = dp[nn-2][1] + dp[nn-2][2]
        dp[nn][3] = dp[nn-3][1] + dp[nn-3][2] + dp[nn-3][3]
    return sum(dp[n])

T = int(input().rstrip())
tmp = 0
dp = [[0, 0, 0, 0] for _ in range(10000+1)]
for _ in range(T):
    n = int(input().rstrip())

    if n > tmp:
        print(solution(n))
    else:
        print(sum(dp[n]))
    tmp = n
