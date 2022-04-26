import sys
from collections import deque

def solution(subin, dest):
    q = deque()
    q.append(subin)
    position = [0 for _ in range(dest*5)]
    position[subin] =  1
    while q:
        curr = q.popleft()
        if curr == dest:
            print(position[curr])
            break
        if position[curr] % 2 != 0:
            if subin - 1 >= 0:
                q.append(curr-1)
                position[curr-1] = position[curr]+1
            if subin + 1 <= dest:
                q.append(curr+1)
                position[curr + 1] = position[curr] + 1
        else:
            q.append(curr*2)
            position[curr*2] = position[curr]+1
        print("pos = ",position)

if __name__ == '__main__':
    subin, dest = map(int,(sys.stdin.readline().split(' ')))
    print(subin, dest)
    solution(subin, dest)
