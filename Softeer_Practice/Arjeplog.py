#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=411
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def melt_time(x, y, matx):
    visit = [[0] * x for _ in range(y)]
    vis_pos = []
    for yy in range(y):
        for xx in range(x):
            if matx[yy][xx] == 0 and visit[yy][xx] == 0:
                for d in range(4):
                    tx = xx + dx[d]
                    ty = yy + dy[d]
                    if 0 <= tx < x and 0 <= ty < y:
                        if matx[ty][tx] == 1:
                            visit[ty][tx] += 1
                            vis_pos.append((ty, tx))
    for v in vis_pos:
        vy, vx = v
        if visit[vy][vx] >= 2:
            matx[vy][vx] = 0
    for m in matx:
        if 1 in m:
            return True

    return False


y, x = map(int, sys.stdin.readline().split(' '))
matx = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(y)]

sec = 0
while melt_time(x, y, matx):
    sec += 1
    for m in matx:
        print(m)
    print()
print(sec + 1)