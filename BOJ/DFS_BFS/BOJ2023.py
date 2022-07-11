# https://www.acmicpc.net/problem/2023
#from collections import defaultdict
N = int(input().rstrip())

# 두 번째 시도
# 재귀호출하여 조건에 맞지 않는 숫자는 탐색하지 않도록 함
ans = []

def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def dfs(num, cnt):
    global ans
    if cnt == N:
        ans.append(num)
        return
    tmp = num * 10
    for i in range(1, 10):
        if check_prime(tmp+i) == True:
            dfs(tmp+i, cnt + 1)
        else:
            continue

for n in range(2, 10):
    if check_prime(n) == True:
        dfs(n, 1)
print(*ans, sep='\n')

# 첫 번째 시도
# 시간초과 문제 발생
'''        
start = int('2' * N)
end = int('1' + '0' * N)
prime_list = defaultdict(int)
        
def prime_num (num):
    cnt = 0
    for n in range(1, N+1):
        tmp = int(num[:n])
        #if tmp in prime_list:
        if prime_list[tmp] != 0:
            cnt += 1
        else:
            for i in range(2, tmp):
                if tmp % i == 0:
                    return False
            cnt += 1
            prime_list[tmp] += 1
    if cnt == N:
        return True
    else:
        return False
ans = []
for num in range(int(start), int(end)):
    if prime_num(str(num)) == True:
        ans.append(num)
print(*ans, sep='\n')
'''