# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=623
import sys

M, N, K = list(map(int, sys.stdin.readline().split()))
scret_key = list(map(int, sys.stdin.readline().split()))
user_key = list(map(int, sys.stdin.readline().split()))

# 시간초과
def secret():
    if M > N:
        print("normal")
        return

    idx = 0
    while True:
        f_idx = 0
        for u in range(len(user_key[idx:])):
            if user_key[u] == scret_key[0]:
                f_idx = u + idx
                break
        if f_idx > N - M:
            print("normal")
            break
        flg = True
        for s in range(1, len(scret_key)):

            if scret_key[s] != user_key[f_idx + s]:
                flg = False
                break

        if flg == False:
            idx = f_idx + 1
            continue
        else:
            print("secret")
            break

# 통과
def secret2():
    if M > N:
        print("normal")
        return

    for u in range(len(user_key)):
        if user_key[u] == scret_key[0]:
            idx = 1
            while idx != M:
                if u + idx >= N:
                    print("normal")
                    return
                if user_key[u+idx] == scret_key[idx]:
                    idx += 1
                else:
                    idx = -1
                    break
            if idx == M:
                print("secret")
                return
    print("normal")
    return

secret2()