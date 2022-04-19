#https://www.acmicpc.net/problem/7576
# 토마토

def stack_solution(n, m, board):    # n : x축, m : y축
    ans = 0
    tmt = []                                #토마토 위치 좌표
    def find_tmt():                         #토마토 위치를 찾는 함수
        for mm in range(m):
            for nn in range(n):
                if board[mm][nn] == 1:
                    tmt.append([mm,nn])
    find_tmt()

    stk = []                                #방문할 장소를 담을 리스트
    stk.extend(tmt)
    new_stk = []


    while len(stk) != 0:
        tmt = stk.pop()
        if board[tmt[0]][tmt[1]] == 0:
            board[tmt[0]][tmt[1]] = 1

        for i in range(-1,2):
            for j in range(-1,2):
                if i*j != 0:
                    continue
                y = tmt[0] + i
                x = tmt[1] + j
                if x > n-1 or y > m-1:
                    continue
                if x < 0 or y < 0:
                    continue
                if board[y][x] == 0:
                    if [y,x] not in new_stk:
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





if __name__ == '__main__':
    x, y = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(y)]
    print(stack_solution(x, y, board))