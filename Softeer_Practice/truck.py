#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=631
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    size_compare = 0
    offers = []
    for _ in range(n):
        tmp = []
        offer_tmp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        offer_tmp = offer_tmp[1:]
        for of in range(len(offer_tmp)):
            if of % 2 == 0:
                if size_compare < offer_tmp[of]:
                    size_compare = offer_tmp[of]
                tmp.append([offer_tmp[of], offer_tmp[of+1]])
            else:
                continue
        offers.append(tmp)


    szmax = size_compare
    expense = [0 for _ in range(szmax)]
    m = int(sys.stdin.readline().rstrip())
    goal = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    ans = [0 for _ in range(len(goal))]
    for i in range(szmax):
        sum = 0

        for of in offers:
            idx = -1
            tmp = 0

            for off in range(len(of)):
                if of[off][0] <= i+1:     #신차 크기보다 고객 요구한 사이즈가 작을 경우
                    if tmp <= of[off][1]:
                        tmp = of[off][1]
                        idx = off
            if idx != -1:
                sum += of[idx][1]
        if sum >= goal[i]:
            expense[i] = sum
        else:
            expense[i] = sum

    id = 0
    flg = False
    for g in goal:
        for ee in range(len(expense)):
            if expense[ee] >= g:
               ans[id] = (ee+1)
               flg = True
               break
        if flg == False:
            ans[id] = (-1)
        id += 1
        flg = False


    for a in ans:
        print(a, end=' ')


solution()