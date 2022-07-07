# https://www.acmicpc.net/problem/1520
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

v, h = map(int, sys.stdin.readline().split())
mat = [[0 for _ in range(h)] for _ in range(v)]

for i in range(v):
    mat[i] = list(map(int, sys.stdin.readline().split()))

#dp[y][x] : (y, x) 에서 (v-1, h-1) 까지 도달할 수 있는 방법의 수
dp = [[-1 for _ in range(h)] for _ in range(v)]

def dfs2(y, x):
    if x == h-1 and y == v-1:
        # 목표좌표에 도달하면 현재 dfs를 호출한 dp[y`][x`]의 값을 1증가
        return 1
    if dp[y][x] != -1:
        # 현재 좌표가 이미 방문한 적 있는 곳이면 이전에 누적된 dp[y][x] ((y,x)에서 목표좌표까지 도달할 수 있는 방법의 수)를 더해줌
        return dp[y][x]
    # 현재 좌표가 처음 방문하는 곳이라면 0으로 초기화
    # 0으로 초기화 이후 아래 for문에서 경로를 탐색하고 목표 좌표까지 도달 가능한 경로라면 +, 도달 가능한 경로가 없다면 그대로 0
    # 그리고 dp[y][x] 를 리턴
    dp[y][x] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < h and 0 <= yy < v and mat[y][x] > mat[yy][xx]:
            dp[y][x] += dfs2(yy, xx)

    return dp[y][x]

print(dfs2(0, 0))