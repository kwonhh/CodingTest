#https://www.acmicpc.net/problem/1700
import sys

n, k = list(map(int, sys.stdin.readline().split()))     # n 멀티탭 구멍 갯수, k 총 사용 횟수
pattern = list(map(int, sys.stdin.readline().split()))
holes = [-1] * n
idx_h = 0
idx_p = 0
while idx_h < n:
    if pattern[idx_p] not in holes and holes[idx_h] != pattern[idx_p]:
        holes[idx_h] = pattern[idx_p]
        idx_h += 1
        idx_p += 1
    else:
        idx_p += 1
#print("h",holes)
idx_p = 0
ans = 0
while idx_p != k :
    # 시도3
    # 현재부터 다음 사용까지의 거리가 가장 먼 코드를 우선으로 뽑도록 함
    # 아래 else문에서 if holes[idx_h] == pp 일 경우 그냥 break 하기 떄문에
    # 다음 사용까지의 거리가 가장 긴 경우는 존재하지 않는 경우임
    if pattern[idx_p] in holes:
        idx_p += 1
    else:
        idx_h = 0
        dist_m = 0
        idx_h_m = -1
        while idx_h != n:
            dist = 0
            for pp in pattern[idx_p:]:
                if holes[idx_h] == pp:
                    break
                else:
                    dist += 1
            if dist == 0:
                #print(idx_h_m, idx_h)
                idx_h_m = idx_h
                break
            elif dist > dist_m:
                dist_m = dist
                idx_h_m = idx_h
            idx_h += 1
        holes[idx_h_m] = pattern[idx_p]

        ans += 1

    '''
    # 시도2 : 현재 코드가 나중에 쓰이는지 안쓰이는지만 확인했더니, 꽂힌 콘센트가 모두 사용될 경우에 대한 처리가 애매해짐
    # 그래서 나중에 몇번 쓰이는지 횟수를 카운트하고, 카운트 값이 가장 적은 코드를 뽑도록 함
    if pattern[idx_p] in holes:
        idx_p += 1
    else:
        idx_h = 0
        cnt_t = 101
        idx_h_t = -1
        while idx_h != n:
            cnt = 0
            for p in pattern[idx_p:]:
                if p == holes[idx_h]:
                    cnt += 1
            if cnt == 0:
                idx_h_t = idx_h
                break
            elif cnt_t >= cnt:
                cnt_t = cnt
                idx_h_t = idx_h
            idx_h += 1
        holes[idx_h_t] = pattern[idx_p]
        ans += 1
    '''
    '''
        # 시도1 : 단순하게 지금 현재의 장치를 나중에도 쓰는지 확인하고, 안쓰면 뽑도록 한 코드
            if holes[idx_h] in pattern[idx_p:]:
                idx_h += 1
            else:
                break
        if idx_h == n:
            idx_h -= 1
        holes[idx_h] = pattern[idx_p]
    
        ans += 1
    '''
print(ans)