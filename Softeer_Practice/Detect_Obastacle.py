#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=409
import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def surroundings(edge, matx):
    q = deque()
    ans = []

    for yy in range(edge):
        for xx in range(edge):
            area = 0
            if matx[yy][xx] == '1':
                q.append((yy, xx))
                vis = []
                while q:
                    curry, currx = q.popleft()
                    if (curry, currx) not in vis and matx[curry][currx] == '1':
                        area += 1
                        vis.append((curry, currx))
                        matx[curry][currx] = '0'
                    else:
                        continue
                    for d in range(4):
                        ambx = currx + dx[d]
                        amby = curry + dy[d]

                        if ambx >= 0 and amby >= 0 and ambx < edge and amby < edge:
                            if matx[amby][ambx] == '1' and (amby, ambx) not in vis:
                                q.append((amby, ambx))
                ans.append(area)

    print(len(ans))
    sorted_ans = sorted(ans)
    for a in sorted_ans:
        print(a)


edge = int(sys.stdin.readline().rstrip())
matx = [list(sys.stdin.readline().rstrip()) for _ in range(edge)]

surroundings(edge, matx)