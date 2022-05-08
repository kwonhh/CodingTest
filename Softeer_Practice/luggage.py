# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=581
import sys
from itertools import permutations
num_of_rail, box_weight, repeat = list(map(int, sys.stdin.readline().split()))
rails = list(map(int, sys.stdin.readline().split()))


'''
# 무게 범위가 크지 않아서 계수 정렬로 오름차순 정렬하고
# 풀면 답이 나올 것이라고 생각했는데 오답
# 그래서 다른 여러가지 경우를 모두 고려했는데 첫번째 예제 기준 어떻게 풀어도 답이 62가 나옴
# 결국 구글링 한 결과 브루트포스 알고리즘으로 풀어야 한다는 것을 확인
tmp = [0 for _ in range(50+1)]
for r in rails:
    tmp[r] += 1
sorted_rails = []
for t in range(1, 51):      # 문제에서 택배 상자 무게의 최대는 50이라고 주어짐
    if tmp[t] == 1:
        sorted_rails.append(t)
    if len(sorted_rails) == num_of_rail:
        break
print(sorted_rails)

ans = 0
idx = 0
w_tmp = 0
repeat_t = 0
while repeat_t != repeat:
    idx = idx % num_of_rail
    w_tmp += sorted_rails[idx]
    if w_tmp > box_weight:
        ans += (w_tmp - sorted_rails[idx])
        print(w_tmp, sorted_rails[idx])
        w_tmp = sorted_rails[idx]
        repeat_t += 1
    idx += 1
print(ans)
'''
ans = 0
pm = permutations(rails, num_of_rail)
for p in pm:
    idx = 0
    bx = 0
    rpt = 0
    ans_tmp = 0
    while rpt != repeat:
        bx += p[idx % num_of_rail]
        if bx > box_weight:
            ans_tmp += (bx - p[idx % num_of_rail])
            if ans != 0 and ans_tmp > ans:
                break
            rpt += 1
            bx = p[idx % num_of_rail]
        idx += 1
    if ans == 0:
        ans = ans_tmp
    elif ans != 0 and ans > ans_tmp:
        #print("p ", p)
        ans = ans_tmp
print(ans)