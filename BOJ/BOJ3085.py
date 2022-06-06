# https://www.acmicpc.net/problem/3085

n = int(input().rstrip())

candy = []
for _ in range(n):
    candy.append(list(input().rstrip()))
#print(candy)
ans = 0

#ret_list = []
direction = [0, (-1, 0), (1,0), (0, -1), (0,1)]

def solution3(current, x, y, sum, visit, dir, flg):
    visit.append((x, y))
    global ans
    if candy[y][x] == current or flg == True:
        x_tmp = x + direction[dir][1]
        y_tmp = y + direction[dir][0]
        if 0 <= x_tmp < n and 0 <= y_tmp < n :
            if candy[y_tmp][x_tmp] == current and ((x_tmp, y_tmp) not in visit) :
                solution3(current, x_tmp, y_tmp, sum+1, visit, dir, flg)
            elif flg == False and candy[y_tmp][x_tmp] != current and (x_tmp, y_tmp) not in visit:
                if dir == 1 or dir == 2:
                    if (x_tmp-1 >= 0 and candy[y_tmp][x_tmp-1] == current) or (x_tmp+1 < n and candy[y_tmp][x_tmp+1] == current):
                        solution3(current, x_tmp, y_tmp, sum+1, visit, dir, True)
                    else:
                        #ret_list.append(sum)
                        ans = max(ans, sum)

                    if 1 <= y_tmp < n - 1:
                        if (dir == 1 and candy[y_tmp-1][x] == current) or (dir == 2 and candy[y_tmp+1][x] == current):
                            #ret_list.append(sum+1)
                            ans = max(ans, sum+1)

                else:
                    if (y_tmp-1 >= 0 and candy[y_tmp-1][x_tmp] == current) or (y_tmp+1 < n and candy[y_tmp+1][x_tmp] == current):
                        solution3(current, x_tmp, y_tmp, sum+1, visit, dir, True)
                    else:
                        #ret_list.append(sum)
                        ans = max(ans, sum)
                    if 1 <= x_tmp < n - 1:
                        if (dir == 3 and candy[y][x_tmp-1] == current) or (dir == 4 and candy[y][x_tmp+1] == current):
                            # ret_list.append(sum+1)
                            ans = max(ans, sum + 1)
            else:
                #ret_list.append(sum)
                ans = max(ans, sum)
        else:
            #ret_list.append(sum)
            ans = max(ans, sum)

    elif candy[y][x] != current:
        #ret_list.append(sum)
        ans = max(ans, sum)

for y in range(n):
    for x in range(n):
        current = candy[y][x]
        for i in range(1, 5):
            sum = 1
            visit = []
            flg = False
            solution3(current, x, y, sum, visit, i, flg)


#print(max(ret_list))
print(ans)