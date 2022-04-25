#https://www.acmicpc.net/problem/6603
#로또

from itertools import permutations
from collections import deque
import sys

def dfs(numbers, comb, res):
    for n in numbers:
        if n not in comb:
        #comb.append(n)
            if len(comb) == 6:
                comb.sort()
                if comb not in res:
                    for c in comb:
                        print(c, end = ' ')
                    print()

                    res.append(comb)
                return
            #11째 줄이 문제였음, 재귀 종료 조건을 만족하고 원래 상태로 돌아오면 comb에 이미 이전의 n이 append되어있으니까
            # 1,2, .. / 1,3... / 1,4... 등 순차적으로 진행된게 아니고 1번만 실행
            dfs(numbers, comb + [n], res)

def lotto_solution(permutation, numbers):
    res = []
    for p in permutation:
        tmp = []
        for r in range(len(p)):
            if p[r] == 1:
                tmp.append(numbers[r])
        res.append(tmp)
    res.sort()
    for r in res:
        for rr in r:
            print(rr, end=' ')
        print()
    print()

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    '''
    while 1:
        line = sys.stdin.readline()
        line2int = list(map(int, line.split()))
        if line2int[0] == 0 :
            break

        numbers = line2int[1:]
        num = len(numbers)
        p = [1]*num
        for r in range(6, num):
            p[r] = 0
        permutation = list(set(permutations(p)))
        #lotto_solution(permutation, numbers)
    '''

    while True:
        input = sys.stdin.readline()
        numbers = list(map(int, input.split()))
        if numbers[0] == 0:
            break
        res = []
        for n in numbers[1:]:
            dfs(numbers, [n], res)
        print()
        #for nn in range(len(numbers[1:])):
        #    dfs(numbers[1+nn:], [numbers[nn]], res)

        #for r in res:
        #    print(r)
        #print()
    #numbers = [1,2,3,5,8,13,21,34]
    #numbers = [1, 2, 3, 4]



'''
#https://www.acmicpc.net/problem/6603
#로또

from itertools import permutations
from collections import deque
import sys

def dfs(numbers, comb, res):
    for n in numbers:
        if n not in comb:
            #comb.append(n)
            if len(comb) == 6:
                comb.sort()
                for c in comb:
                    print(c, end=' ')
                print()
                res.append(comb)
                #comb.sort()
                #if comb not in res:
                #    res.append(comb)
                return
            #11째 줄이 문제였음, 재귀 종료 조건을 만족하고 원래 상태로 돌아오면 comb에 이미 이전의 n이 append되어있으니까
            # 1,2, .. / 1,3... / 1,4... 등 순차적으로 진행된게 아니고 1번만 실행
            dfs(numbers, comb + [n], res)


def dfs_solution(numbers, line, res):
    print("curr = ", line[-1], " line = ", line, "  res = ", res)
    #if len(line) == 6:
        #line.sort()
        #print(line)
        #return line
        #res.append(line)

    print(line)
    for n in numbers:
        if n not in line:
            line.append(n)

            dfs_solution(numbers, line, res)
            print("dfs 이후 : line = ", line, " n = ", n)
            if len(line) == 6:
                line.sort()
                res.append(line)
                return line
            if len(line) > 6:
                return line
def lotto_solution(permutation, numbers):
    res = []
    for p in permutation:
        tmp = []
        for r in range(len(p)):
            if p[r] == 1:
                tmp.append(numbers[r])
        res.append(tmp)
    res.sort()
    for r in res:
        for rr in r:
            print(rr, end=' ')
        print()
    print()

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    
    while True:
        input = sys.stdin.readline()
        numbers = list(map(int, input.split()))
        if numbers[0] == 0:
            break
        res = []
        #for n in numbers[1:]:
        #    dfs(numbers, [n], res)
        for nn in range(len(numbers[1:])):
            dfs(numbers[1+nn:], [numbers[nn]], res)

        #for r in res:
        #    print(r)
        #print()
    #numbers = [1,2,3,5,8,13,21,34]
    #numbers = [1, 2, 3, 4]




'''


