# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=391
import sys
sys.setrecursionlimit(10000)
virus, p, times = list(map(int, sys.stdin.readline().split()))
times *= 10
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
'''
pp = pow(p,5)
ret = 1
for t in range(times):
    ret *= pp
    ret %= 1000000007

print(virus*ret*ret)
'''
def ret_virus(p, times):
    if times >= 1000000:
        times = times // 2
    ret = 1
    for _ in range(times):
        ret *= p
        ret = ret % 1000000007
    return ret * ret_virus(p, times)

ans = ret_virus(p, times)
print(ans)