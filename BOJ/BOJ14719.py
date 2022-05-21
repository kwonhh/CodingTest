#https://www.acmicpc.net/problem/14719

import sys

h, w = list(map(int, sys.stdin.readline().split()))
wall = list(map(int, sys.stdin.readline().split()))

def find_wall(wall, idx, width):
    idx_l = idx - 1
    idx_r = idx + 1
    r_flg = False
    l_flg = False
    while idx_l >= 0:
        if wall[idx_l] > 0:
            l_flg = True
            break
        idx_l -= 1
    while idx_r < width:
        if wall[idx_r] > 0:
            r_flg = True
            break
        idx_r += 1
    return l_flg & r_flg

ans = 0
while h > 0:
    for ww in range(w):
        if wall[ww] <= 0 and find_wall(wall, ww, w) == True:
            ans += 1
    for ww in range(w):
        wall[ww] -= 1
    h -= 1
print(ans)

