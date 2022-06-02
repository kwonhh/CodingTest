# https://www.acmicpc.net/problem/1197

import sys

n_node, n_edge = map(int, sys.stdin.readline().split())
tree = []
checker = [0] * (n_node + 1)
vis = [0] * n_node
for nn in range(1, n_node+1):
    checker[nn] = nn


'''
# 실패했던 find 함수
def find (node):
    if checker[node] == node:
        #if node2 > node1:
        #    return node1
        return node
    else:
        root = find(checker[node])
        #if root > node1:
        #    return node1
        return root
'''
def find (node):
    if checker[node] != node:
        checker[node] = find(checker[node])
    return checker[node]

def union (a_node, b_node):
    a = find(a_node)
    b = find(b_node)
    if a == b:
        return 0
    if a > b:
        checker[checker[a_node]] = b
        checker[a_node] = b
    else:
        checker[checker[b_node]] = a
        checker[b_node] = a
    return 1


for _ in range(n_edge):
    a, b, cost = map(int, sys.stdin.readline().split())
    if a > b:
        tree.append((b,a,cost))
    else:
        tree.append((a,b,cost))

s_tree = sorted(tree, key=lambda x:x[2])
ans = 0
leng = 0
num = 0
for s in range(n_edge):
    if union(s_tree[s][0], s_tree[s][1]) == 0:
        continue
    else:
        ans += s_tree[s][2]
    leng += 1
    if leng == n_node - 1:
        break
print(ans)
