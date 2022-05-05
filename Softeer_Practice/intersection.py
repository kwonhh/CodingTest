#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=803

import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline().rstrip())
    info = deque()
    q = deque()
    for _ in range(n):
        i, c = list(sys.stdin.readline().rstrip().split(' '))
        info.append([int(i), c])

    time = info[0][0]
    ans = [0 for _ in range(n)]
    prior = 0

    stk = [0 for _ in range(4)]
    flg = True
    while flg:
        if len(info) != 0 and time == info[0][0]:
            tmpi, tmpc = info.popleft()
            if tmpc == 'A':
                stk[0] += 1
            elif tmpc == 'B':
                stk[1] += 1
            elif tmpc == 'C':
                stk[2] += 1
            elif tmpc == 'D':
                stk[3] += 1
            q.append([tmpc, prior])
            prior += 1
            continue

        coin = False
        idx_sum = 0
        stk_val = 0


        for s in range(4):
            if stk[s] != 0:
                stk_val += 1
                idx_sum += s
        if stk_val == 4:
            for qt in q:
                if qt[0] != 'X':
                    ans[qt[1]] = -1
            break
        if idx_sum % 2 == 0:
            coin = True
        elif idx_sum == 0:
            break

        for qq in range(len(q)):
            if q[qq][0] == 'X':
                continue
            if q[qq][0] == 'B' or q[qq][0] == 'D':
                if q[qq][0] == 'B':
                    if stk[0] == 0:
                        stk[1] -= 1
                        q[qq][0] = 'X'
                        ans[q[qq][1]] = time
                    else:
                        ans[q[qq][1]] = -1
                    if coin == False:
                        time += 1
                        break
                    else:
                        continue

                if q[qq][0] == 'D':
                    if stk[2] == 0:
                        stk[3] -= 1
                        q[qq][0] = 'X'
                        ans[q[qq][1]] = time
                    else:
                        ans[q[qq][1]] = -1
                        continue
                    if coin == False:
                        time += 1
                        break
                    else:
                        continue



            elif q[qq][0] == 'A' or q[qq][0] == 'C':
                if q[qq][0] == 'A':
                    if stk[3] == 0:
                        stk[0] -= 1
                        q[qq][0] = 'X'
                        ans[q[qq][1]] = time
                    else:
                        ans[q[qq][1]] = -1
                    if coin == False:
                        time += 1
                        break
                    else:
                        continue
                if q[qq][0] == 'C':
                    if stk[1] == 0:
                        stk[2] -= 1
                        q[qq][0] = 'X'
                        ans[q[qq][1]] = time
                    else:
                        ans[q[qq][1]] = -1
                    if coin == False:
                        time += 1
                        break
                    else:
                        continue
        if coin == True:
            time += 1

        if len(q) == n:
            for qa in q:
                if qa[0] == 'X':
                    flg = False
                else:
                    flg = True

    for a in ans:
        print(a)

solution()

