import sys
from collections import deque

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

def find_route(m, n, graph):
    ans = 1
    stk = deque()
    stk.append([0,0])
    #visit = deque()
    new_stk = deque()
    while len(stk) != 0:
        pos = stk.popleft()
        #visit.append(pos)
        graph[pos[0]][pos[1]] = 2

        if pos[0] == m-1 and pos[1] == n-1:
            #break
            return ans

        for i in range(4):
            dx = pos[1] + x[i]
            dy = pos[0] + y[i]
            if dy > m-1 or dx > n-1 or dy < 0 or dx < 0:
                continue
            if graph[dy][dx] == 1:
                #if [dy, dx] not in visit and [dy, dx] not in stk:
                new_stk.append([dy, dx])
        if len(stk) == 0:
            ans += 1
            #stk.extend(new_stk)
            stk += new_stk
            #new_stk = deque()
            new_stk = []
    print(ans)

if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    # m 이 y축, n 이 x축
    graph = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(m)]
    print(find_route(m, n, graph))

