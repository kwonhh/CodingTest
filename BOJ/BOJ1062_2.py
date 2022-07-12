# https://www.acmicpc.net/problem/1062
from itertools import combinations
n, k = map(int, input().split())

# 남극에 존재하는 n개의 단어에 대하여 각 단어의 비트마스킹 값을 저장하기 위한 리스트
word_b = [0] * n
for i in range(n):
    tmp = input().rstrip()
    for j in tmp:
        # anta [...] tica 를 한 글자씩 비트로 변환하여 더해줌
        word_b[i] |= (1 << (ord(j) - ord('a')))
req = 0
for i in 'antic':
    # 남극의 글자를 읽기 위해서 anta, tica 를 무조건 알고 있어야 하므로
    # antatica에서 중복을 제거한 antic을 비트마스킹 하여 req에 저장
    req |= (1 << (ord(i) - ord('a')))

mx = 0
# 위 antic을 제외한 나머지 알파벳
will_teach = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
if k < 5:
    print(0)
else:
    for c in list(combinations(will_teach, k-5)):
        curr = 0
        cnt = 0
        # will_teach에 저장된 알파벳 중 임의의 k-5개를 뽑아 만들 수 있는 알파벳의 조합을 구함
        # 구한 알파벳 조합을 비트 마스킹 하여 새로 배우게 될 단어에 대한 비트마스킹 값을 curr에 저장
        for comb in c:
            curr |= (1 << (ord(comb) - ord('a')))
        # antic 다섯개의 알파벳은 필수로 알아야 하므로 curr과 req를 or연산
        curr |= req
        for wb in word_b:
            if wb & curr == wb:
                # 현재의 단어 조합 curr에는 anti[..will_teach에서 k-5개를 뽑아 만든 알파벳 조합..]tica에 대한 비트마스킹이 저장되어 있고
                # curr 과 남극의 단어 wb를 and 연산 했을 때의 값이 wb인지
                # 즉, curr을 배웠을 때 wb를 읽을 수 있는지를 확인하고, 읽을 수 있다면 cnt값을 증가
                cnt += 1
        # cnt 값이 최대값이라면 mx 값을 갱신
        mx = max(mx, cnt)
    print(mx)