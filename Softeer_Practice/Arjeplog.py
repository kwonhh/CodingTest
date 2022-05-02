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

def melt_time(x, y, graph, second):
    # 굳이 매번 전체 행렬을 탐색할 이유가 없을 것 같아서
    # 얼음의 좌표 찾을 때만 전체 행렬 돌면서 각 좌표를 덱에 담아주고,
    # 반복문을 통해 그 덱만 순환하도록 구현해봄

    # 얼음이 존재하는 좌표 탐색
    ice = deque()
    melt = []
    for yy in range(y):
        for xx in range(x):
            if graph[yy][xx] == 1:
                ice.append((yy, xx))
    new_ice = deque()
    while len(ice) != 0:
        curry, currx = ice.popleft()
        edge = 0
        for d in range(4):
            amby = curry+dy[d]
            ambx = currx+dx[d]
            if amby >= 0 and ambx >= 0 and amby < y and ambx < x:
                if graph[amby][ambx] == 0 and (amby, ambx) not in melt:
                    edge += 1
                else:
                    continue
                ambyy = amby + dy[d]
                ambxx = ambx + dx[d]
                if ambyy >= 0 and ambxx >= 0 and ambyy < y and ambxx < x:
                    if graph[ambyy][ambxx] == 1 and (ambyy, ambxx) not in melt:
                        edge -= 1

            #print("new ice", new_ice)
        if edge >= 2:
            print("(curry, currx) = (", curry, " , ", currx, ")")
            graph[curry][currx] = 0
            melt.append((curry, currx))
        else :
            new_ice.append((curry, currx))
        if len(ice) == 0:
            print("new ice ", new_ice)
            for g in graph:
                print(g)
            print(new_ice)
            ice.extend(new_ice)
            new_ice.clear()
            melt.clear()
            second += 1
    print("second :: ", second)

y,x = map(int, sys.stdin.readline().split(' '))
matx = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(y)]

sec = 0
#melting_time(x, y, matx, sec)
melt_time(x, y, matx, sec)