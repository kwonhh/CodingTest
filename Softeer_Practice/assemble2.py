#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=404
import sys

def solution():
    line, factory = list(map(int,sys.stdin.readline().split()))
    time = [0 for _ in range(factory)]
    prevtime = [0 for _ in range(factory)]

    for _ in range(line-1):
        tmp = list(map(int, sys.stdin.readline().split()))
        cmp = []
        for ff in range(factory):
            #(tmp[ff], tmp[ff+factory], prevtime[ff])
            cmp.append(tmp[ff] + tmp[ff+factory]+prevtime[ff])
            #print("cmp ", cmp)
        for ff in range(factory):
            cmpt = cmp[:]
            cmpt[ff] = prevtime[ff]+tmp[ff]
            #print("cmpt  ",cmpt)
            time[ff] = min(cmpt)
            prevtime[ff] = time[ff]
            #print("time ", time)
    tmp2 = list(map(int, sys.stdin.readline().split()))
    for t in range(len(tmp2)):
        time[t] += tmp2[t]

    ans = min(time)
    print(ans)

solution()