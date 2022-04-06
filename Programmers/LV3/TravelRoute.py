

def solution(tickets):
    used = []
    graph = ["ICN"]
    answer = []
    while len(graph) != 0:
        tmp = graph.pop()
        answer.append(tmp)
        candidate = []
        for t in tickets:
            if tmp == t[0]:
                if t not in used:
                    candidate.append(t)
        candidate.sort()
        # print(candidate)
        if len(candidate) > 0:
            graph.append(candidate[0][1])
            used.append(candidate[0])

    return answer

# 미해결