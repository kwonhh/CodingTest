import sys
from collections import deque

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

def find_route(m, n, graph, visit):
    stk = deque()
    stk.append([0,0])
    while len(stk) != 0:
        posy, posx = stk.popleft()

        if posy == m-1 and posx == n-1:
            print(visit[m-1][n-1]+1)
            break
        for i in range(4):
            dx = posx + x[i]
            dy = posy + y[i]
            if dy < m and dx < n and dy >= 0 and dx >= 0:
                if visit[dy][dx] == 0 and graph[dy][dx] != 0:
                    stk.append([dy, dx])
                    visit[dy][dx] = visit[posy][posx]+1


if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    # m 이 y축, n 이 x축
    graph = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(m)]
    visit = [[0]*n for _ in range(m)]
    find_route(m, n, graph, visit)

