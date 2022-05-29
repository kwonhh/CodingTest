# https://www.acmicpc.net/problem/1197
import sys

n_node, n_edge = map(int, sys.stdin.readline().split())
tree = []
checker = [0] * (n_node + 1)
vis = [0] * n_node
for nn in range(1, n_node+1):
    checker[nn] = nn

def find (node1, node2):
    if checker[node2] == node2:
        if node2 > node1:
            return node1
        return node2
    else:
        root = find(node1, checker[node2])
        if root > node1:
            return node1
        return root

def union (node, root):
    new_node = checker[node]
    checker[node] = root
    if checker[new_node] != root:
        union(new_node, root)


for _ in range(n_edge):
    a, b, cost = map(int, sys.stdin.readline().split())
    if a > b:
        tree.append((b,a,cost))
    else:
        tree.append((a,b,cost))

s_tree = sorted(tree, key=lambda x:x[2])
#print(s_tree)
ans = 0
leng = 0
num = 0
for s in range(n_edge):
    if checker[s_tree[s][0]] == checker[s_tree[s][1]]:
        continue

    root = find(checker[s_tree[s][0]], checker[s_tree[s][1]])
    union(s_tree[s][0], root)
    union(s_tree[s][1], root)

    ans += s_tree[s][2]
    leng += 1
    #print("check = ", checker, "(", s_tree[s][0]," <--> ", s_tree[s][1], ")")
    if leng == n_node - 1:
        break
print(ans)
