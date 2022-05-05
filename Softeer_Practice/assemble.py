#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=403
import sys
'''
ans = 0
min_idx = -1
min = 10000
num_of_line = int(sys.stdin.readline().rstrip())
tmp = [[]]*2
idx1 = 0
idx2 = 1
for nn in range(num_of_line):
    t_idx = nn % 2
    tmp[t_idx]=(list(map(int, sys.stdin.readline().split())))

    if nn < 1:
        continue
    else:
        cmp = [0] * 4

        cmp[0] = tmp[idx1][0]+tmp[idx2][0]            # An -> An+1
        cmp[1] = tmp[idx1][1]+tmp[idx1][3]+tmp[idx2][0]    # Bn -> tn -> An+1
        cmp[2] = tmp[idx1][1]+tmp[idx2][1]            # bn -> Bn+1
        cmp[3] = tmp[idx1][0]+tmp[idx1][2]+tmp[idx2][1]    # An -> tn -> Bn+1
        idx1 = ~idx1
        idx2 = ~idx2

        if min_idx != -1:
            if min_idx < 2:
                cmp[1] = 0
                cmp[2] = 0
            else:
                cmp[0] = 0
                cmp[3] = 0

        for c in range(len(cmp)):
            if cmp[c] != 0 and cmp[c] < min:
                min = cmp[c]
                min_idx = c
        ans += min


print(ans)
'''
def solution():
    line = int(sys.stdin.readline().rstrip())
    ta = 0
    tb = 0
    preva = 0
    prevb = 0
    for _ in range(line-1):
        tmp = list(map(int, sys.stdin.readline().split()))
        ta = min(tmp[0]+preva, tmp[1]+tmp[3]+prevb)
        tb = min(tmp[1]+prevb, tmp[0]+tmp[2]+preva)
        preva = ta
        prevb = tb
    tmp = list(map(int, sys.stdin.readline().split()))
    ta += tmp[0]
    tb += tmp[1]

    ans = min(ta, tb)
    print(ans)

solution()