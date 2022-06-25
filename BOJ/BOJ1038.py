# https://www.acmicpc.net/problem/1038
import sys

n = int(sys.stdin.readline().rstrip())
if n >= 1023:
    print(-1)
else:
    max_num = '9876543210'
    ans = []
    for i in range(1,1024):
        tmp = i
        str_i = ''
        while tmp > 1:
            str_i = str(tmp % 2) + str_i
            tmp //= 2
        str_i = str(tmp) + str_i
        tmp_s = ''
        for s in range(len(str_i),0,-1):
            if str_i[(s*(-1))] == '1':
                tmp_s += max_num[(s*(-1))]
        ans.append(int(tmp_s))


    ans.sort()
    print(ans[n])
