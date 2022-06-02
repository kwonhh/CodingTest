# https://www.acmicpc.net/problem/2252
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
prior_table = [0] * (n+1)
nedge_table = [[] for _ in range(n+1)]
edge = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nedge_table[a].append(b)
    edge.append((a, b))
for mm in range(m):
    prior_table[edge[mm][1]] += 1
q = deque()
for nn in range(1, n+1):
    if prior_table[nn] == 0:
        q.append(nn)

ans = []
while q:
    current = q.popleft()
    ans.append(current)

    # 시도1
    npop = 0
    # 현재 노드에 연결된 엣지를 돌면서
    for n in range(len(nedge_table[current])):
        if nedge_table[current][n] == 0:
            # 연결된 노드의 값이 0이면(== 엣지가 끊어졌으면) continue
            continue
        # 위 조건을 만족하지 않으면 해당 노드의 차수를 1 감소시키고
        prior_table[nedge_table[current][n]] -= 1
        if prior_table[nedge_table[current][n]] == 0:
            #그때 그 차수가 0이라면 q에 노드를 추가시켜 줌
            q.append(nedge_table[current][n])
        # 여기까지 완료되었으면 해당 노드의 값을 0으로 (엣지가 끊어졌음을 의미) 바꿔줌
        nedge_table[current][n] = 0

    '''
    #시도 2 : 더 간단한 방법으로 작성한 코드
    for i in nedge_table[current]:
        prior_table[i] -= 1
        if prior_table[i] == 0:
            q.append(i)
    '''
print(*ans)

