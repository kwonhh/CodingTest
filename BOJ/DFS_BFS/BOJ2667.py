# https://www.acmicpc.net/problem/2667
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().rstrip())))
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(x, y):
    vis = []
    ret = 0
    s = deque()
    s.append((x, y))
    while s:
        curr_x, curr_y = s.pop()
        if (curr_x, curr_y) not in vis:
            ret += 1
        vis.append((curr_x, curr_y))
        mat[curr_y][curr_x] = -1
        for i in range(4):
            new_x = dir[i][1] + curr_x
            new_y = dir[i][0] + curr_y
            if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in vis:
                if mat[new_y][new_x] == 1:
                    s.append((new_x, new_y))
    return ret

ans = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            ans.append(solution(j, i))
ans.sort()
print(len(ans))
for a in ans:
    print(a)
