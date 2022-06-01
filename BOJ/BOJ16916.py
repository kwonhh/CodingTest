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
            # 문자가 불일치 하는 지점을 찾고,
            # 일치했던 부분 문자열의 길이(match)에서 접두사=접미사인 길이(pi[match-1])를 빼주고, 그 값을 begin에 대입하여 다음 탐색 진행
            # 이때 pi[match-1] 이 0이면 match되었던 문자열 다음부터 진행함을 의미하고,
            #                    0이 아니면, 접두사=접미사인 길이는 굳이 다시 확인할 필요가 없으니까, 그 값을 jump하여 각각 p와 s를 비교하겠다는 의미
            begin += (match - pi[match-1])
            # 접두사=접미사 길이인 pi[match-1]은
            # 이전 단계에서 match 된 문자열의 길이와 동일하므로
            # (즉, 0이 아닌 경우에는 굳이 처음부터 비교할 필요 없이, match가 지시하는 부분 문자열 위치부터 확인이 이뤄짐)
            # 이 값을 match에 대입해주고, 그 상태에서 탐색 진행
            match = pi[match-1]
print(ans)