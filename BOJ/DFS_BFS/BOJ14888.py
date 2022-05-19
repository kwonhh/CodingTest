#https://www.acmicpc.net/problem/14888
import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
#print("n = ", n)
#print("nums ", nums)
#print("op ", op)
values = []
def dfs(value, idx, op):
    if idx == n-1:
        values.append(value)
        return
    for o in range(4):
        if op[o] != 0:
            if o == 0:
                tmp = op[:]
                tmp[o] -= 1
                dfs(value + nums[idx+1], idx+1, tmp)

            elif o == 1:
                tmp = op[:]
                tmp[o] -= 1
                dfs(value - nums[idx+1], idx+1, tmp)

            elif o == 2:
                tmp = op[:]
                tmp[o] -= 1
                dfs(value * nums[idx+1], idx+1, tmp)

            elif o == 3:
                tmp = op[:]
                tmp[o] -= 1
                val_tmp = 0
                if value < 0:
                    val_tmp = (((-1) * value) // nums[idx+1]) * (-1)
                    dfs(val_tmp, idx+1, tmp)
                else:
                    dfs(value // nums[idx+1], idx+1, tmp)


idx = 0
value = nums[idx]
dfs(value, idx, op)
print(max(values))
print(min(values))