def solution(numbers, target):
    answer = 0
    graph = []
    num = len(numbers)
    for n in range(num):
        if n == 0:
            tmp = []
            tmp.append(numbers[0])
            tmp.append(numbers[0] * (-1))
            graph.append(tmp)
            continue
        order = []
        for gg in graph[n - 1]:
            order.append(gg + numbers[n])
            order.append(gg - numbers[n])
        graph.append(order)
    # print(graph)
    for a in graph[-1]:
        if a == target:
            answer += 1

    return answer