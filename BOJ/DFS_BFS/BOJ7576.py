#https://www.acmicpc.net/problem/7576
# 토마토
import sys
from collections import deque

def find_tmt(n, m):  # 토마토 위치를 찾는 함수
    tmt = deque()
    for mm in range(m):
        for nn in range(n):
            if board[mm][nn] == 1:
                tmt.append([mm, nn])
    return tmt

def dfs_solution(n, m, board):    # n : x축, m : y축
    ans = 0
    tmt = find_tmt(n,m)             #토마토 위치 좌표
    stk = deque()
    stk.extend(tmt)
    new_stk = deque()
    rng = [-1, 0, 1]


    while len(stk) > 0:
        tmt = stk.pop()
        if board[tmt[0]][tmt[1]] == 0:
            board[tmt[0]][tmt[1]] = 1

        for i in rng:
            for j in rng:
                if i*j != 0:
                    continue
                y = tmt[0] + i
                x = tmt[1] + j
                if x > n-1 or y > m-1:
                    continue
                if x < 0 or y < 0:
                    continue
                if board[y][x] == 0:
                    #if [y,x] not in new_stk:
                    new_stk.append([y,x])


        if len(stk) == 0:
            if len(new_stk) == 0:
                break
            stk.extend(new_stk)
            new_stk = []
            ans += 1
    for b in board:
        if 0 in b:
            ans = -1
            break

    return ans


def bfs_solution(n, m, board):
    ans = 0
    q = deque()
    tmt = find_tmt(n, m)  # 토마토 위치 좌표
    q.extend(tmt)

    rng = [-1, 0, 1]
    while len(q) > 0:
        tmt = q.popleft()
        if board[tmt[0]][tmt[1]] == 0:
            board[tmt[0]][tmt[1]] = 1

        for i in rng:
            for j in rng:
                if i + j > 1 or i + j < -1 or i + j == 0:
                    continue
                y = tmt[0] + i
                x = tmt[1] + j
                if y < 0 or y > m-1:
                    continue
                if x < 0 or x > n-1:
                    continue
                if board[y][x] == 0:
                    q.append([y, x])
                    board[y][x] = board[tmt[0]][tmt[1]]+1

    for b in board:
        if 0 in b:
            return -1

        ans = max(ans, max(b))      # b는 board의 각 행, 각 행마다 최댓값을 찾고 이 값을 ans와 비교하여 더 큰 값을 ans에 담기
    return ans-1



if __name__ == '__main__':
    n, m = [int(x) for x in sys.stdin.readline().split()]
    board = deque()
    for _ in range(m):
        board.append([int(x) for x in sys.stdin.readline().split()])
    #print(dfs_solution(n, m, board))
    print(bfs_solution(n, m, board))