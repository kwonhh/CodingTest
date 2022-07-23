# https://www.acmicpc.net/problem/9470
from collections import deque

T = int(input().rstrip())


def make_list(st, ed):
    in_degree[ed] += 1
    l_list[st].append(ed)
    src[ed].append(st)

def solution(q):
    while q:
        start, order = q.popleft()
        vis.append(start)
        p.append(start)
        for n in l_list[start]:
            in_degree[n] -= 1
            if n not in vis and in_degree[n] == 0:
                q.append((n, order+1))

def solution2(q):
    while q:
        start, order = q.popleft()
        vis.append(start)
        for n in l_list[start]:
            in_degree[n] -= 1
            if tmp[n] == order:
                tmp[n] += 1
            else:
                tmp[n] = max(tmp[n], order)
            if n not in vis and in_degree[n] == 0:
                q.append((n, tmp[n]))

def solution3(q):
    solution(q)
    for pp in p:
        if len(src[pp]) != 0:
            for s in src[pp]:
                if tmp[pp] != tmp[s]:
                    tmp[pp] = max(tmp[pp], tmp[s])
                else:
                    tmp[pp] += 1
    #print(tmp[p[-1]])
    return tmp[p[-1]]

for _ in range(T):
    K, M, P = map(int, input().split())
    in_degree = [0 for _ in range(M + 1)]
    l_list = [[] for _ in range(M + 1)]
    tmp = [0 for _ in range(M + 1)]
    src = [[] for _ in range(M + 1)]
    vis = []
    p = deque()
    for _ in range(P):
        st, ed = map(int, input().split())
        make_list(st, ed)
    q = deque()
    for m in range(1, M + 1):
        if in_degree[m] == 0:
            tmp[m] = 1
            q.append((m, tmp[m]))

    print(K, solution3(q))
