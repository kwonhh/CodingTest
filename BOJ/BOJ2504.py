#https://www.acmicpc.net/problem/2504
import sys
from collections import deque

inp = deque(sys.stdin.readline().rstrip())

def solution(inp):
    s = deque()
    while inp:
        tmp1 = inp.popleft()
        if tmp1 != ']' and tmp1 != ')':
            s.append(tmp1)
        elif tmp1 == ']':
            if len(s) == 0:
                print(0)
                return
            sum = 0
            cnt = 0
            while s:
                tmp2 = s.pop()
                if tmp2 != '[':
                    if tmp2 == '(':
                        print(0)
                        return
                    cnt += 1
                    sum += tmp2
                else:
                    if cnt != 0:
                        sum *= 3
                        s.append(sum)
                    else:
                        s.append(3)
                    break
        elif tmp1 == ')':
            if len(s) == 0:
                print(0)
                return
            sum = 0
            cnt = 0
            while s:
                tmp2 = s.pop()
                if tmp2 != '(':
                    if tmp2 == '[':
                        print(0)
                        return
                    cnt += 1
                    sum += tmp2
                else:
                    if cnt != 0:
                        sum *= 2
                        s.append(sum)
                    else:
                        s.append(2)
                    break
    ans = 0
    for ss in s:
        if ss == '(' or ss == ')' or ss == '[' or ss  == ']':
            print(0)
            return
        ans += ss
    print(ans)


solution(inp)



