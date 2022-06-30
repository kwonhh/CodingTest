# https://www.acmicpc.net/problem/9095

N = int(input().rstrip())

def solution(n):
    if n < 3:
        print(n)
        return

    p = [0 for _ in range(n+1)]
    p[0] = 1
    p[1] = 1
    p[2] = 2

    for i in range(3, n+1):
        for j in range(i-3, i):
            p[i] += p[j]
    print(p[n])

for _ in range(N):
    n = int(input().rstrip())
    solution(n)