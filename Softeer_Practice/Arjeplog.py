#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=411
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def melting_time(x, y, matx, sec):
    stk = deque()
    cand = []
    # 얼음이 녹은게 1초 전이 아니고 이번에 녹았을 경우를 표시하기 위한 리스트
    for yy in range(y):
        for xx in range(x):
            edge = 0
            if matx[yy][xx] == 1:
                for d in range(4):
                    tmp_x = xx + dx[d]
                    tmp_y = yy + dy[d]
                    if tmp_x > -1 and tmp_y > -1 and tmp_y < y and tmp_x < x:
                        if matx[tmp_y][tmp_x] == 0 and (tmp_y, tmp_x) not in cand:
                            edge += 1
                            tmp_xx = tmp_x + dx[d]
                            tmp_yy = tmp_y + dy[d]
                            if tmp_xx > -1 and tmp_yy > -1 and tmp_xx < x and tmp_yy < y:
                                if matx[tmp_yy][tmp_xx] == 1 or (tmp_yy, tmp_xx) in cand:
                                    #얼음이 둘러쌓인 곳인지 확인하기 위한 조건
                                    edge -= 1
                    if edge >= 2:
                        matx[yy][xx] = 0
                        cand.append((yy, xx))
                        break
                if edge < 2:
                    stk.append((yy, xx))

    if len(stk) != 0:
        melting_time(x, y, matx, sec+1)
    else :
        print("sec = ",sec+1)

y,x = map(int, sys.stdin.readline().split(' '))
matx = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(y)]

sec = 0
melting_time(x, y, matx, sec)