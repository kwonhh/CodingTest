#https://www.acmicpc.net/problem/1062
#문제의 의도를 잘 모르겠음...;
import sys
from itertools import combinations
default_list = ['a', 'c', 'i', 'n', 't']

n, k = list(map(int, sys.stdin.readline().split()))
alp = [0  for _ in range(27)]
antatica = ['a', 'n', 't', 'a', 't', 'i', 'c', 'a']
for aa in antatica:
    alp[ord(aa) - 96] += 1
cnt = 5

input_list = []
ans = 0

for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    input_list.append(tmp[4:-4])

def solution(alp, word, ref):
    cnt_tmp = 0
    global cnt
    for ww in word:
        if alp[ord(ww)-96] == 0:
            cnt_tmp += 1
        alp[ord(ww)-96] += 1
    if cnt + cnt_tmp <= ref:
        cnt += cnt_tmp
        return 1
    else:
        for ww in word:
            alp[ord(ww)-96] -= 1
        return 0

for i in input_list:
    ans += solution(alp, i, k)
print(ans)




