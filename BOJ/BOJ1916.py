# https://www.acmicpc.net/problem/1916
import sys
INF = int(1e9)
graph = []
n = int(sys.stdin.readline().rstrip())       # 도시의 갯수
m = int(sys.stdin.readline().rstrip())       # 버스의 갯수

for _ in range(m):
    departure, arrival, cost = map(int, sys.stdin.readline().split())
    graph.append((departure, arrival, cost))
    # (시작도시, 도착도시, 비용)
dep, arr = map(int, sys.stdin.readline().split()) # 문제에서 요구하는 출발 도시, 도착 도시
#print("n = ", n, " m = ", m, "\ngraph = ", graph, "\ndeparture = ", dep, "arrival = ", arr)

dist = [INF] * (n+1)

def bf(start):
    dist[start] = 0
    for _ in range(n-1):
        flg = 0
        for mm in range(m):
            curr_node = graph[mm][0]
            next_node = graph[mm][1]
            cost = graph[mm][2]
            if dist[curr_node] != INF and dist[next_node] > dist[curr_node] + cost:
                dist[next_node] = dist[curr_node] + cost
                flg += 1
        if flg == 0:
            break

bf(dep)
print(dist[arr])
