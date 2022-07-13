# https://www.acmicpc.net/problem/16197
import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
h, w = list(map(int, sys.stdin.readline().split()))
grp = []
for _ in range(h):
    grp.append(list(list(sys.stdin.readline().rstrip())))

def find_ball():
    pos = []
    for i in range(h):
        for j in range(w):
            if grp[i][j] == 'o':
                pos.append([i, j])
    return pos
b1, b2 = find_ball()

def bfs(pos1, pos2):
    ans = 1
    vis = []
    q = deque()
    q.append((pos1, pos2, ans))
    while q:
        b1, b2, ans_c= q.popleft()
        if ans_c > 10:
            print(-1)
            return
        vis.append((b1, b2))
        b1y, b1x = b1
        b2y, b2x = b2
        pos1_ = []
        pos2_ = []
        for i in range(4):
            n1y = b1y + dy[i]
            n1x = b1x + dx[i]
            n2y = b2y + dy[i]
            n2x = b2x + dx[i]
            if 0 <= n1y < h and 0 <= n1x < w:
                if grp[n1y][n1x] != '#':
                    pos1_ = [n1y, n1x]
                else:
                    pos1_ = [b1y, b1x]
            else:
                if 0 <= n2y < h and 0 <= n2x < w:
                    print(ans_c)
                    return
                else:
                    continue

            if 0 <= n2y < h and 0 <= n2x < w:
                if grp[n2y][n2x] != '#':
                    pos2_ = [n2y, n2x]
                else:
                    pos2_ = [b2y, b2x]
            else:
                if 0 <= n1y < h and 0 <= n1x < w:
                    print(ans_c)
                    return
                else:
                    continue
            if (pos1_, pos2_) not in vis and pos1_ != pos2_:
                q.append((pos1_, pos2_, ans_c+1))
        # 문제 조건은 10보다 큰 경우에 -1을 출력하도록 했는데
        # 10을 포함시키는 바람에 42%에서 계속 오답
        # 그것도 모르고 다른 부분을 집중해서 보는 바람에 푸는데 생각보다 시간이 더 걸렸다
        if ans_c > 10:
            print(-1)
            return

    print(-1)
    return

bfs(b1, b2)
