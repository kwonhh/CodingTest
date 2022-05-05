#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=413

import sys


def loop_solution(iter):
    prev = 2
    start = 3
    if iter == 1:
        print(start*start)
        return start*start
    for i in range(1,iter):
        tmp = start
        start += prev
        prev = tmp
    print(start*start)

def recv_solution(iter):
    if iter == 1:
        return 3
    if iter == 0:
        return 2
    if iter < 0:
        return
    return recv_solution(iter-1) + recv_solution(iter-2)


a = int(sys.stdin.readline().rstrip())
ans = recv_solution(a)
print(ans*ans)

