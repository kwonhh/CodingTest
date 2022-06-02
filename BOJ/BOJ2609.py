#https://www.acmicpc.net/problem/2609
import sys

n, m = list(map(int, sys.stdin.readline().split()))
big = 0
small = 0
if n > m :
    big = n
    small = m
else:
    big = m
    small = n
ans1 = 0
ans2 = 0
for s in range(1, small+1):
    if big % s == 0 and small % s == 0:
        ans1 = s
ans2 = ans1 * (big // ans1) * (small // ans1)

print(ans1)
print(ans2)