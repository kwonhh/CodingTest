

def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visit = []
    while len(stack) != 0:
        tmp = stack.pop()
        if tmp == target:
            break
        answer += 1
        for w in words:
            for l in range(len(tmp)):
                if w[:l] + w[l+1:] == tmp[:l] + tmp[l+1:]:
                    if w not in visit:
                        visit.append(w)
                        stack.append(w)
    if tmp == target:
        return answer
    else:
        return 0

