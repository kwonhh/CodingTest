import sys
from collections import deque

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

def find_route(m, n, graph, stk, ans, vis=[]):
    while stk:
        pos = stk.popleft()
        if pos[0] == m-1 and pos[1] == n-1:
            print(ans)
            return
        graph[pos[0]][pos[1]] = -1
        vis.append(pos)
        new_stk = deque()

        for i in range(4):
            dx = pos[1]+x[i]
            dy = pos[0]+y[i]
            if dy > m-1 or dx > n-1 or dy < 0 or dx < 0:
                continue
            if graph[dy][dx] == 1 and [dy, dx] not in vis:
                new_stk.append([dy, dx])
        if len(new_stk) != 0:
            find_route(m, n, graph, new_stk, ans+1, vis)
        else:
            return


if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    # m 이 y축, n 이 x축
    graph = []
    stk = deque()
    stk.append([0,0])
    vis = []
    ans = 0

    for _ in range(m):
        input1 = sys.stdin.readline().rstrip()
        tmp = []
        for i in input1:
            tmp.append(int(i))
        graph.append(tmp)
    find_route(m, n, graph, stk, ans, vis)
    for g in graph:
        print(g)

