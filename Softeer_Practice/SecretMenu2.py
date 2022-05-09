# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=633
import sys

N, M, K = list(map(int, sys.stdin.readline().split()))      # N : 첫 번째 입력의 길이, M : 두 번째 입력의 길이, K : 버튼의 최대 범위
if N > M:
    lng = list(map(int, sys.stdin.readline().split()))
    sht = list(map(int, sys.stdin.readline().split()))
elif N <= M:
    sht = list(map(int, sys.stdin.readline().split()))
    lng = list(map(int, sys.stdin.readline().split()))

same = [[0] * len(sht) for _ in range(len(lng))]

longest = 0
for ll in range(len(lng)):
    for ss in range(len(sht)):
        if lng[ll] == sht[ss]:
            if ll > 0 and ss > 0:
                same[ll][ss] = same[ll-1][ss-1] + 1
            else:
                same[ll][ss] += 1
        if same[ll][ss] > longest:
            longest = same[ll][ss]

print(longest)