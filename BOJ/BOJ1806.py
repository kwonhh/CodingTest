#https://www.acmicpc.net/problem/1806
import sys


n, s = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

'''
#시도 1
#길이 2일때부터 순차적으로 찾아갔더니 시간초과 발생
start = 2
ans = 0
g_sum = nums[0]
while start != n+1:
    #print("st ", start)
    g_sum += nums[start-1]
    sum_ = g_sum
    #print("sum_ = ", sum_)
    if sum_ >= s:
        ans = start
        break
    for nn in range(1, n-start+1):
        sum_ += (nums[nn+1] - nums[nn-1])
        if sum_ >= s:
            ans = start
            break
    if ans != 0:
        break
    start += 1
print(ans)
'''
'''
#시도 2
start = n//2
ans = 0
g_sum = sum(nums[0:start])
while 1 < start < n+1:
    flg = False
    #g_sum = sum(nums[0:start])
    if g_sum >= s:
        if start == n:
            ans = start
            break
        start_prev = start
        start //= 2
        g_sum -= sum(nums[start+1:start_prev+1])
        if start != 1:
            ans = start
        flg = True
        continue
    else:
        sum_ = g_sum
        for ss in range(1, n - start+1):
            sum_ += (nums[start+ss-1] - nums[ss-1])
            #print("nums[start+ss-1 (",start,"+",ss-1, " )] = ", nums[start+ss-1], "  nums[ss-1(",ss-1,")] = ", nums[ss-1], "sum_ = ", sum_)
            if sum_ >= s:
                start //= 2
                g_sum -= sum(nums[start + 1:start_prev+1])
                flg = True
                break
        if flg != True:
            if (n-start) // 2 == 0:
                #g_sum += sum(nums[start:])
                g_sum += sum(nums[start_prev + 1:start + 1])
                start += 1
            else:
                start_prev = start
                start += (n-start) // 2
                #print("start = ", start)
                g_sum += sum(nums[start_prev+1:start+1])
                continue
        if start != 1:
            ans = start
    if start > n:
        ans = 0
        break
print(ans)
'''
#시도 3 : 시간초과 해결되지 않아서 찾아보니 "Two Pointer"란 알고리즘이 있었고, 그것을 적용해서 풀어봄
start = 0
end = 0
sum = 0
ans = n+1
flg = False
while start != n or end != n:
    if start == end:
        sum = nums[start]

    if sum >= s or flg:
        if ans > end - start + 1:
            ans = end - start + 1
        start += 1
        if start == n:
            break
        sum -= nums[start-1]
    else:
        if end < n-1:
            end += 1
            sum += nums[end]
            flg = False
        else:
            # end 포인터가 끝까지 도달한 이후에
            # sum 이 s보다 작다면 더이상 start를 증가시켜도 당연히 s보다 작기 때문에
            # (start를 증가시킬 때는 sum에서 nums[start]를 빼는 작업이기 때문에)
            # 반복문 빠져나온다
            break

if ans > n:
    ans = 0
print(ans)
