
# 미해결
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


# 재시도
def solution(tickets):
    answer = []
    visit = []
    graph = ["ICN"]
    graph_stack = []
    while len(graph) != 0:
        depart = graph.pop()
        answer.append(depart)
        if len(answer) == len(tickets) + 1:
            break
        if len(graph_stack) != 0:
            visit.append(graph_stack.pop())
        cand = []
        candList = []
        for t in tickets:
            if t[0] == depart and t not in visit:
                cand.append(t[1])
                graph_stack.append(t)
        cand.sort(reverse=True)
        graph_stack.sort(reverse=True)
        graph += cand
        #print(graph)
    return answer