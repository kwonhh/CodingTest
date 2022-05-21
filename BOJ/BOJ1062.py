#https://www.acmicpc.net/problem/1062
import sys


def solution2(alp, word, ref, vis, word_):
    if word_ in vis:
        return 0
    vis.append(word_)
    global cnt
    if cnt > ref:
        return 0
    cnt_t = 0
    for w in word:
        if alp[ord(w)-96] == 0:
            cnt_t += 1
        alp[ord(w)-96] += 1

    if cnt + cnt_t <= ref:
        cnt += cnt_t
        return 1
    else:
        for w in word:
            alp[ord(w) - 96] -= 1
        return 0

n, k = list(map(int, sys.stdin.readline().split()))
antatica = ['a', 'n', 't', 'a', 't', 'i', 'c', 'a']
alp = [0  for _ in range(27)]

for aa in antatica:
    alp[ord(aa) - 96] += 1

i_list = []
ans = 0
cnt = 5
for _ in range(n):
    tmp = sys.stdin.readline()
    i_list.append(tmp[4:-5])
list(set(i_list))
i_list.sort()
#print(i_list)

def solution(alp, word, ref):
    cnt_tmp = 0
    global cnt
    for w in word:
        if alp[ord(w)-96] == 0:
            cnt_tmp += 1
    if cnt + cnt_tmp <= ref:
        cnt += cnt_tmp
        for w in word:
            alp[ord(w)-96] += 1
        return 1
    else:
        return 0

if k < 5:
    print(0)
else:
    for i in i_list:
        ans += solution(alp, i, k)
    print(ans)