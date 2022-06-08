# https://www.acmicpc.net/problem/2294
import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.sort()
dp = [0 for _ in range(k+1)]
for j in range(1, k+1):
    if j % coin[0] == 0:
        dp[j] = j // coin[0]

for i in range(1, n):
    for j in range(coin[i], k+1):
        tmp = j % coin[i]
        if tmp == 0 and (dp[j] == 0 or dp[j] > j // coin[i]):
            # tmp == 0 : 현재 코인으로 j를 만들 수 있으면서, 동시에 기존 dp[j] 값보다 coin[i]의 갯수가 적다면 새로운 값으로 갱신
            dp[j] = j // coin[i]
        elif tmp != 0 and dp[j - coin[i]] != 0 and (dp[j] == 0 or dp[j] > 1 + dp[j - coin[i]]):
            # 현재 코인으로 j를 만들 수 없지만, 나머지 값을 다른 코인을 활용하여 만들 수 있다면 값을 갱신
            # dp[j] 와 1 + dp[j-coin[i] 를 비교하여 가장 적은 갯수가 맞는지 확인
            # 이때 dp[j-coin[i]]는 현재 코인의 가치를 제외한 나머지 값에 대하여, 다른 코인들을 활용하여 만들 수 있는 최소 갯수
            dp[j] = 1 + dp[j - coin[i]]

if dp[k] == 0:
    print(-1)
else:
    print(dp[k])