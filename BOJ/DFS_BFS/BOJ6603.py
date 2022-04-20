#https://www.acmicpc.net/problem/6603
#로또

from itertools import permutations
import sys


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
        lotto_solution(permutation, numbers)

