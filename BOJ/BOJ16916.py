# https://www.acmicpc.net/problem/16916
p = input().rstrip()
s = input().rstrip()

pi = [0] * (len(s))
i = 0
j = 1
while j < len(s):
    if s[i] != s[j]:
        while i > 0:
            # i가 0이 될 때까지 pi[i-1]을 확인하면서 j가 가리키는 문자와 동일한지 확인
            i = pi[i-1]
            if s[i] != s[j]:
                continue
            else:
                pi[j] = i + 1
                i += 1
                break
    else:
        pi[j] = i + 1
        i += 1
    j += 1

match = 0
begin = 0
ans = 0
while match < len(s) and begin + match < len(p):
    if p[begin + match] == s[match]:
        match += 1
        if match == len(s):
            ans = 1
            break
    else:
        if match == 0:
            begin += 1
        else:
            # 문자가 불일치 하는 지점을 찾고, match가 0이 아니라면
            # 일치했던 부분 문자열의 길이(match)에서 접두사=접미사인 길이를 빼주고, 그 값을 begin에 대입하여 다음 탐색 진행
            begin += (match - pi[match-1])
            # match는 이전 접두사=접미사 길이를 대입해주고, 그 상태에서 탐색 진행
            match = pi[match-1]
print(ans)