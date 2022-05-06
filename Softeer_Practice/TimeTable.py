# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=392
import heapq
import sys

num = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(num):
    start, finish = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(heap, (finish, start))
ans = 0
ref = 0
while heap:
    fin, st = heapq.heappop(heap)
    if st >= ref:
        ans += 1
        ref = fin
print(ans)
