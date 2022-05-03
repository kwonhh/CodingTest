#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=403
import sys

a_line = []
b_line = []
a_delay = [0]
b_delay = [0]
number_of_line = int(sys.stdin.readline().rstrip())

for n in range(number_of_line):
    tmp = list(map(int, sys.stdin.readline().split(' ')))
    if len(tmp) == 2:
        a_line.append(tmp[0])
        b_line.append(tmp[1])
        a_delay.append(0)
        b_delay.append(0)
    else:
        a_line.append(tmp[0])
        b_line.append(tmp[1])
        a_delay.append(tmp[2])
        b_delay.append(tmp[3])

def solution(num_of_line, a_line, b_line, a_delay, b_delay):
    ans = 0

    for n in range(num_of_line-1):
        # a라인에서만 생산했을 경우 / n 시점에는 a라인을 이용하고 n+1 시점에는 b라인을 이용하는 경우를 비교
        timea = min(a_line[n]+a_line[n+1], a_line[n]+a_delay[n+1]+b_line[n+1])
        # b라인에서만 생산했을 경우 / n 시점에는 b라인을 이용하고 n+1 시점에는 a라인을 이용하는 경우를 비교
        timeb = min(b_line[n]+b_line[n+1], b_line[n]+b_delay[n+1]+a_line[n+1])

        # 공장 라인이 3개 이상인 경우 : 0이 아닌 n 시점에서 n-1 시점에서의 라인 생산시간이 중복 가산되기 때문에 이 값을 빼줌
        if timea > timeb:
            ans += timeb
            if n != 0:
                ans -= b_line[n]
        else:
            ans += timea
            if n != 0:
                ans -= a_line[n]
    print(ans)

solution(number_of_line, a_line, b_line, a_delay, b_delay)