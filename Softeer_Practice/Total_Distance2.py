#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=635

import sys
from collections import defaultdict, deque

def total_distance():
    num_of_node = int(sys.stdin.readline().rstrip())
    graph = defaultdict(list)
    for _ in range(num_of_node -1):
        tmp = list(map(int, sys.stdin.readline().split(' ')))
        graph[tmp[0]].append((tmp[1], tmp[2]))
        graph[tmp[1]].append((tmp[0], tmp[2]))
    print(graph)
    q = deque()
    def ret_dist(graph, start, dest):

        q = deque()
        q.append(start)
        visit = deque()
        sum = 0
        while q:
            node = q.popleft()

            for gg in graph[node]:
                if gg[0] not in visit:
                    sum += gg[1]
        print("start = ", start, " dest = ", dest, " sum = ", sum)
        return sum

    ans = [0 for _ in range(num_of_node)]
    for i in range(1, num_of_node+1):
        tmp = 0
        for j in range(1, num_of_node + 1):
            if i == j:
                continue
            tmp += ret_dist(graph, i, j)
        ans[i-1] = tmp
    print(ans)

total_distance()
