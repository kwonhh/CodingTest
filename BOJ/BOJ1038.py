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
        # 10진수를 2진수의 string으로 변환
        while tmp > 1:
            str_i = str(tmp % 2) + str_i
            tmp //= 2
        str_i = str(tmp) + str_i
        # 변환된 2진수 문자열과 '9876543210'을 마스킹하여 ans 리스트에 수를 추가
        # '9876543210'에서 n개를 선택하는 경우, 가능한 경우의 수 중에서 감소하는 수는 1개일 수밖에 없음
        tmp_s = ''
        for s in range(len(str_i),0,-1):
            if str_i[(s*(-1))] == '1':
                tmp_s += max_num[(s*(-1))]
        ans.append(int(tmp_s))


    ans.sort()
    print(ans[n])
