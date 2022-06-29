# https://www.acmicpc.net/problem/17070
import sys

#아무리해도 89%에서 시간초과 문제가 해결되지 않아 DP 방법으로 풀어서 통과
h_size = int(sys.stdin.readline().rstrip())
home = [[] for _ in range(h_size)]
for h in range(h_size):
    home[h] = list(map(int, sys.stdin.readline().split()))

HRZ = 1     # 가로
VTC = 2     # 세로
CRS = 3     # 대각선

ans = 0
def pipe_solution(end):
    global ans
    y, x, d = end
    if x == h_size - 1 and y == h_size - 1:
        ans += 1
        return
    if x + 1 < h_size and y + 1 < h_size:
        if home[y][x+1] == 0 and home[y+1][x] == 0 and home[y+1][x+1] == 0:
            pipe_solution((y+1, x+1, CRS))
    if d != VTC:
        if x + 1 < h_size:
            if home[y][x+1] == 0:
                pipe_solution((y, x+1, HRZ))
    if d != HRZ:
        if y + 1 < h_size:
            if home[y+1][x] == 0:
                pipe_solution((y+1, x, VTC))

dp = [[[0 for _ in range(h_size)] for _ in range(h_size)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, h_size):
    if home[0][i] == 0 and dp[0][0][i-1] == 1:
        # home 에서 0 이고(= 벽이 아니고), dp[0][0][i-1]이 1인 경우(=이전 움직임이 있었던 경우)
        dp[0][0][i] = 1

def dp_solution(dp):
    for y in range(1, h_size):
        for x in range(2, h_size):
            if home[y][x] != 0:
                #현재 위치 (y, x)가 벽이라면 건너뜀
                continue
            # 가로 방향의 dp[0][y][x]는 dp[0][y][x-1] 와 dp[2][y][x-1] 로부터 옮겨진 것
            # dp[0][y][x-1] : x방향으로 1 이전 위치에서 옮기는 경우
            # dp[2][y][x-1] : 이전에 대각선 방향으로 옮긴 것이 (y, x-1) 위치에 있는 경우
            dp[0][y][x] += (dp[0][y][x-1] + dp[2][y][x-1])

            # 세로 방향의 dp[0][y][x]는 dp[1][y-1][x] 와 dp[2][y-1][x] 로부터 옮겨진 것
            # dp[1][y-1][x] : y방향으로 1 이전 위치에서 옮기는 경우
            # dp[2][y-1][x] : 이전에 대각선 방향으로 옮긴 것이 (y-1, x) 위치에 있는 경우
            dp[1][y][x] += (dp[1][y-1][x] + dp[2][y-1][x])
            if home[y-1][x] == 0 and home[y][x-1] == 0:
                dp[2][y][x] += (dp[0][y-1][x-1] + dp[1][y-1][x-1] + dp[2][y-1][x-1])

#pipe_solution((0, 1, HRZ))
#print(ans)
dp_solution(dp)
print(dp[0][h_size-1][h_size-1]+dp[1][h_size-1][h_size-1]+dp[2][h_size-1][h_size-1])
