
# 시도1
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


# 시도2
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

# 시도3
def DFS(tickets, ticket, visit):
    print("ticket = ", ticket, "  Visit = ", visit)
    visit.append(ticket)
    # if len(visit) == len(ticket):
    # print(visit)
    departure = ticket[1]
    cand = []
    for t in tickets:
        if t[0] == departure:
            if t not in visit:
                cand.append(t)
    cand.sort(reverse=True)
    while len(cand) != 0:
        NewTicket = cand.pop()
        DFS(tickets, NewTicket, visit)
    return visit


def solution(tickets):
    answer = []
    visit = []
    answer_tmp = []
    for t in tickets:
        if t[0] == "ICN":
            answer_tmp = DFS(tickets, t, visit)
    print(answer_tmp)
    for at in answer_tmp:
        answer.append(at[0])
        if at == answer_tmp[-1]:
            answer.append(at[1])
    return answer