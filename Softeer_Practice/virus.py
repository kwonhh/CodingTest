# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=407
import sys
import time

start = time.time()
virus, p, times = list(map(int, sys.stdin.readline().split()))

'''
def ret_multiple(p, times):
    if times == 1:
        return p
    ret = 1
    if times < 1000:
        times_t = times
    else:
        times_t = times // 2
    while times_t != 0:
        ret *= p
        times_t -= 1
    return ret * ret_multiple(p, times-times_t)

times_t = times // 2
ans = virus * (ret_multiple(p, times_t) * ret_multiple(p, times - times_t))
#ans = virus * (ret_multiple(p, times))
end = time.time()
print(ans % 1000000007)
print(end-start)
'''
ret = virus
for t in range(times):
    ret *= p
    ret %= 1000000007

print(ret)
end = time.time()
print(end - start)