# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=394
import sys
from collections import defaultdict, deque

person, edge = list(map(int, sys.stdin.readline().split()))
weight = [0]
weight.extend(list(map(int, sys.stdin.readline().split())))
grp = defaultdict(list)
for _ in range(edge):
    tmp1, tmp2 = list(map(int, sys.stdin.readline().split()))
    grp[tmp1].append(tmp2)
    grp[tmp2].append(tmp1)

ans = 0
q = deque()
vis = [0 for _ in range(person+1)]

for k in range(1, person+1):
    flg = True
    if k not in grp:
        ans += 1
        continue
    for g in grp[k]:
        if weight[k] <= weight[g]:
            flg = False
            break
    if flg:
        ans += 1


print(ans)