# https://www.acmicpc.net/problem/15486
import sys

n = int(sys.stdin.readline().rstrip())
s = [[0, 0] for _ in range(n+1)]
p = [0 for _ in range(n+2)]
for i in range(1, n+1):
    s[i][0], s[i][1] = list(map(int, sys.stdin.readline().split()))

'''
DP p리스트 채우는 방식
-해당 문제는 상담 기간동안은 다른 일을 할 수 없고, 상담을 다 완료하면 돈을 받는 방식
 따라서, 임의 값 a에 대해서 p[a]는 a일까지 일했을 때 벌 수 있는 돈의 최대값이 아니고, "a일 이전까지" 일했을 때 벌 수 있는 돈의 최대값을 의미
-p[a]를 계산하는 방법은 a일에 일을 하거나 안하거나 둘 중 한가지
 일을 안하면 p[a] = p[a+1] 이고 (= a일에 일을 안하고, 다음날로 넘어가는 경우)
 일을 하면   p[a] = p[a] + s[a+s[a][0]][1] (= a일 이전까지 일한 돈의 최대값 + a일에 잡혀있는 상담을 완료할 수 있을 경우 받게 될 돈)
 이 둘 중에서 더 큰 값을 p[a]로 갱신한다
-위 방법으로 마지막날인 n일부터 거꾸로 계산해 내려가고, 계산이 완료되면 p리스트의 최대값을 정답으로 출력
'''

for i in range(n, 0, -1):
    if i + s[i][0] <= n + 1:
        p[i] = max(p[i+s[i][0]] + s[i][1], p[i+1])
    else:
        p[i] = p[i+1]
print(max(p))