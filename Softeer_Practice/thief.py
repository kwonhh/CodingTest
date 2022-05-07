# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=395
import sys
import heapq
from collections import deque

'''
# heapify 함수 이용
# 힙은 root가 최소라는 점 이용해서 root를 pop하면서 리스트에 담고, 역순으로 탐색함
# 통과 못한 코드
def heap_sort(iter):
    heapq.heapify(iter)
    ret = deque()
    while iter:
        ret.append(heapq.heappop(iter))
    return ret

# heapify 는 라이브러리 이용, 힙 sort함수는 직접 구현
# 통과 못한 코드
def heap_sort2(unsorted, size):
    pos = (size // 2) - 1
    heapq.heapify(unsorted)
    for p in range(pos, -1, -1):
        l_pos = 2 * p + 1
        r_pos = 2 * p + 2
        print("left = ", l_pos, "  right = ", r_pos)
        mx_pos = p
        if l_pos < size :
            if unsorted[l_pos][0] > unsorted[pos][0]:
                mx_pos = l_pos
            elif unsorted[l_pos][0] == unsorted[pos][0] and unsorted[l_pos][1] > unsorted[pos][1]:
                mx_pos = l_pos
        if r_pos < size :
            if unsorted[r_pos][0] > unsorted[pos][0]:
                mx_pos = r_pos
            elif unsorted[r_pos][0] == unsorted[pos][0] and unsorted[r_pos][1] > unsorted[pos][1]:
                mx_pos = r_pos
        if mx_pos != p:
            unsorted[pos], unsorted[mx_pos] = unsorted[mx_pos], unsorted[pos]
            if r_pos < size and l_pos < size:
                if unsorted[l_pos][0] > unsorted[r_pos][0]:
                    unsorted[l_pos], unsorted[r_pos] = unsorted[r_pos], unsorted[l_pos]
                elif unsorted[l_pos][0] == unsorted[r_pos][0] and unsorted[l_pos][1] > unsorted[r_pos]:
                    unsorted[l_pos], unsorted[r_pos] = unsorted[r_pos], unsorted[l_pos]
            #heap_sort2(unsorted, size)
            print("p = ", p, " => ", unsorted)
    return unsorted

# heapify랑 heap sort를 직접 구현
# 시간초과 오류 발생
def heap_sort3(unsorted, size):
    for i in range(size):
        c = i
        while c != 0:
            r = (c-1)//2
            if unsorted[c][0] > unsorted[r][0]:
                unsorted[c], unsorted[r] = unsorted[r], unsorted[c]
            elif unsorted[c][0] == unsorted[r][0] and unsorted[c][1] > unsorted[r][1]:
                unsorted[c], unsorted[r] = unsorted[r], unsorted[c]
            c = r
    sz = size // 2 - 1
    for j in range(sz, -1, -1):
        max_pos = j
        l_pos = 2*j + 1
        r_pos = 2*j + 2
        if l_pos < size:
            if unsorted[l_pos][0] > unsorted[max_pos][0]:
                max_pos = l_pos
            #elif unsorted[l_pos][0] == unsorted[max_pos][0] and unsorted[l_pos][1] > unsorted[max_pos][1]:
            #    max_pos = l_pos
        if r_pos < size:
            if unsorted[r_pos][0] > unsorted[max_pos][0]:
                max_pos = r_pos
            #elif unsorted[r_pos][0] == unsorted[max_pos][0] and unsorted[r_pos][1] > unsorted[max_pos][1]:
            #    max_pos = r_pos
        if max_pos != j:
            unsorted[j], unsorted[max_pos] = unsorted[max_pos], unsorted[j]
    return unsorted
'''


W, N = list(map(int, sys.stdin.readline().split()))     # W 가방에 담을 수 있는 최대 무게, N 보석 종류의 수
jw = []
tmp = [0 for _ in range(N+1)]

for _ in range(N):
    m, price = list(map(int, sys.stdin.readline().split()))  # m 보석의 무게, price 보석의 무게 당 가치
    jw.append([price, m])

for j in range(1,len(jw)+1):
    tmp[jw[j-1][0]] += jw[j-1][1]
ans = 0
for t in range(len(tmp)-1, -1, -1):
    if tmp[t] < W:
        ans += t*tmp[t]
    else:
        ans += t*W
    W -= tmp[t]
    if W <= 0:
        break
print(ans)



'''
sorted_jw = (heap_sort(jw))
sorted_jw = heap_sort3(jw, N)
ans = 0
while W >= 0:
    p, w = sorted_jw.popleft()
    N -= 1
    ans += p * w
    W -= w
    heap_sort3(sorted_jw, N)

print(ans)
'''
'''
for j in range(len(sorted_jw)-1, -1, -1):
    #print("j", j)

    if sorted_jw[j][1] <= W:
        ans += sorted_jw[j][0] * sorted_jw[j][1]
        W -= sorted_jw[j][1]
        if W == 0:
            break
    else:
        ans += sorted_jw[j][0] * W
        break

print(ans)
'''

