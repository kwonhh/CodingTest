# https://www.acmicpc.net/problem/1789

s = int(input())
n = 1
ans = 0
if s <= 2:
    ans = 1
else:
    while s >= 0:
        s -= n
        n += 1
        ans += 1
        if s < 0:
            ans -= 1

print(ans)