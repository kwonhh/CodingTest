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
    ans = [0 for _ in range(num_of_node+1)]
    ret_dist(graph, 1, num_of_node, ans)
    print(ans)

def ret_dist(graph, start, num_of_node, ans, visit = deque()):
    print("visit ", visit)
    q = deque()
    q.append(start)
    sum = 0
    while len(visit) != num_of_node:
        node = q.pop()
        visit.append(node)
        if len(graph[node]) == 1 and graph[node][0][0] in visit:
            #재귀
            #값 입력
            ans[graph[node][0][0]] = sum
            print("ddd ", graph[node][0][0])
            ret_dist(graph, start, num_of_node, ans, visit)
            return
        for gg in graph[node]:
            if gg[0] not in visit:
                q.append(gg[0])
                sum += gg[1]

            #sum += sub_sum
            #sub_sum = 0
            #if node == num_of_node:
            #    break
        #print(sum)
        #print(sub_sum)


total_distance()
