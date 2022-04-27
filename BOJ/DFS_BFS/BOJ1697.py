import sys
from collections import deque

def solution(subin, dest):
    visit = [0 for _ in range(100000+1)]
    q = deque()
    q.append(subin)
    while q:
        curr = q.popleft()

        if curr == dest:
            print(visit[curr])
            break

        if 0 <= curr * 2 <= 100000 and visit[curr*2] == 0:
            visit[curr*2] = visit[curr]+1
            #visit[curr * 2] = 1
            q.append(curr*2)
        if 0 <= curr + 1 <= 100000 and visit[curr+1] == 0:
            visit[curr+1] = visit[curr]+1
            #visit[curr + 1] = 1
            q.append(curr+1)
        if 0 <= curr - 1<= 100000 and visit[curr-1] == 0:
            visit[curr-1] = visit[curr]+1
            #visit[curr-1] = 1
            q.append(curr-1)
subin, dest = map(int,(sys.stdin.readline().split(' ')))
solution(subin, dest)
'''
if __name__ == '__main__':
    subin, dest = map(int,(sys.stdin.readline().split(' ')))
    solution(subin, dest)
'''