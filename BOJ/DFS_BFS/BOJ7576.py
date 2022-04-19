#https://www.acmicpc.net/problem/7576
# 토마토

def stack_solution(n, m, board):    # n : x축, m : y축
    ans = 0
    #tmt = [m-1, n-1]
    tmt = []
    def find_tmt():
        for mm in range(m):
            for nn in range(n):
                if board[mm][nn] == 1:
                    tmt.append([mm,nn])

    find_tmt()
    stk = []
    stk.extend(tmt)
    new_stk = []
    '''
    if board[tmt[0] - 1][tmt[1]] == 0:
        stk.append([tmt[0] - 1, tmt[1]])
    if board[tmt[0]][tmt[1] - 1] == 0:
        stk.append([tmt[0], tmt[1] - 1])
    '''

    while len(stk) != 0:
        tmt = stk.pop()
        if board[tmt[0]][tmt[1]] == 0:
            board[tmt[0]][tmt[1]] = 1
        '''
        if tmt[0]-1 >= 0 and tmt[1] >= 0:
            if [tmt[0]-1,tmt[1]] not in vis:
                if [tmt[0]-1,tmt[1]] not in new_stk:
                    if board[tmt[0]-1][tmt[1]] == 0:
                        new_stk.append([tmt[0]-1,tmt[1]])
            if [tmt[0],tmt[1]-1] not in vis:
                if [tmt[0],tmt[1]-1] not in new_stk:
                    if board[tmt[0]][tmt[1]-1] == 0:
                        new_stk.append([tmt[0],tmt[1]-1])
        '''
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