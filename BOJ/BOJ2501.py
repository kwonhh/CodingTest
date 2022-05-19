#https://www.acmicpc.net/problem/2501
import sys

n, m = list(map(int, sys.stdin.readline().split()))
lst = []

for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
if m > len(lst):
    print(0)
else :
    print(lst[m-1])