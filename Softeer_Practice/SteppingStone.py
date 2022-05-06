#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=390
import sys

N = int(sys.stdin.readline().rstrip())
stones = list(map(int, sys.stdin.readline().split()))

st = 0
ans = [0]
def solution():
    for s in range(len(stones)):
        stones[s] = stones[s] / 1000

    for s in range(len(stones)):
        tmp = 1
        idx = 0
        ref = stones[s]
        for ss in stones[s+1:]:
            if ss > ref:
                tmp += 1
                ref = ss
            if N - (s+idx+1) + tmp <= max(ans):
                break
            idx += 1
        ans.append(tmp)
    print(max(ans))

solution()