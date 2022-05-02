#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=408
import sys

numbers = list(map(int, sys.stdin.readline().split(' ')))
ans = ''
if numbers[0] == 1:
    ans = 'ascending'
    for n in range(1,len(numbers)-1):
        if numbers[n] - numbers[n-1] != 1:
            ans = 'mixed'
            break
elif numbers[0] == 8:
    ans = 'descending'
    for n in range(1,len(numbers)-1):
        if numbers[n] - numbers[n - 1] != -1:
            ans = 'mixed'
            break
else:
    ans = 'mixed'

print(ans)