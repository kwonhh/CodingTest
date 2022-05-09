# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=628

import sys


def solution(start, end, service):
    service.sort()
    ans = 0

    # 300MB 이하 서비스의 수 count
    count300 = 0
    for s in service:
        if s <= 300:
            count300 += 1

    # 600MB 초과 서비스의 수 count
    count600 = 0
    for s in service[count300:]:
        if s > 600:
            count600 += 1
    ans += count600

    st = count300
    ed = end - count600

    while st < ed:
        if service[st] + service[ed] <= 900:
            st += 1
            ed -= 1
            ans += 1

        elif count300 > 0:
            count300 -= 1
            ans += 1
            ed -= 1
        else:
            ans += 1
            ed -= 1

    if st == ed:
        if count300 > 0:
            count300 -= 1
        ans += 1

    ans += (count300 + 2) // 3
    print(ans)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    Nserver = int(sys.stdin.readline().rstrip())
    svs = list(map(int, sys.stdin.readline().split()))
    solution(0, Nserver - 1, svs)