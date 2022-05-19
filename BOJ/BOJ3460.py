#https://www.acmicpc.net/problem/3460
import sys

def make_bin(num, idx):
    if num <= 1:
        if num == 1:
            ans.append(idx)
        return
    else:
        if num % 2 == 1:
            ans.append(idx)
        make_bin(num // 2, idx + 1)

numTest = int(sys.stdin.readline().rstrip())
for _ in range(numTest):
    num = int(sys.stdin.readline().rstrip())
    ans = []
    idx = 0


    make_bin(num, idx)

    for a in ans:
        print(a, end=" ")