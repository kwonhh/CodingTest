# https://www.acmicpc.net/problem/2293

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
'''
# 시도1
# 재귀함수로 풀었더니 문제에서 메모리 제한이 4MB이고, 재귀 횟수로 인해 통과하지 못함
visit = []
ans = 0

def solution(sum, comb):
    global ans

    if sum >= k and sorted(comb) not in visit:
        if sum == k:
            #print(comb)
            comb = sorted(comb)
            ans += 1
            visit.append(comb)
    else:
        for c in coin:
            solution(sum+c, comb+str(c))


for c in coin:
    comb = ''
    sum = 0
    solution(sum+c, comb+str(c))

print(ans)
'''

# 시도2
# 메모리와 시간 문제를 해결하기 위해서 인터넷을 참고하니
# Dynamic Programming 방식으로 접근해야 한다는 것을 확인하고, 그 방법을 공부한 뒤 적용
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in range(n):
    for kk in range(1, k+1):
        if kk >= coin[c]:
            dp[kk] = dp[kk] + dp[kk-coin[c]]

print(dp[k])