# https://www.acmicpc.net/problem/12865
n, kg = map(int, input().split())
#dp = [[0 for _ in range(kg+1)] for _ in range(n+1)]
dp = [[0 for _ in range(kg+1)] for _ in range(n+1)]
load = [[0, 0]]
for nn in range(n):
    l, v = map(int, input().split())
    load.append((l, v))

for nn in range(1, n+1):
    for kk in range(1, kg+1):
        if kk < load[nn][0]:
            dp[nn][kk] = dp[nn-1][kk]
        else:
            dp[nn][kk] = max(dp[nn-1][kk], dp[nn-1][kk-load[nn][0]] + load[nn][1])
print(dp[n][-1])

'''
print(2**100)
bit = 2**n
stuff = []
dp = [0 for _ in range(kg+1)]
for _ in range(n):
    tmp1, tmp2 = map(int, input().split())
    stuff.append((tmp1, tmp2))
for b in range(bit):
    tmp = b
    idx = 0
    v = 0
    s = 0
    while idx < n:
        if tmp % 2 != 0:
            #print(idx)
            s += stuff[idx][0]
            v += stuff[idx][1]
            if s > kg:
                break
        #tmp //= 2
        tmp = tmp >> 1
        idx += 1
        if tmp == 0:
            break
    if s <= kg:
        dp[s] = max(dp[s], v)
for d in range(kg, -1, -1):
    if dp[d] != -1:
        print(dp[d])
        break
'''
'''
l = [-1 for _ in range(kg+1)]
for _ in range(n):
    i, value = map(int, input().split())
    l[i] = value

for i in range(1, kg+1):
    s = i
    v = l[i]
    for j in range(i+1, kg+1):
        s += j
        v += l[j]
        if s <= kg:
            l[s] = max(l[s], v)
        else:
            break
print(l)
for ll in range(kg, -1, -1):
    if l[ll] != -1:
        print(l[ll])
        break
'''