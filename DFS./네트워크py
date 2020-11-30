def transper(computers):
    graph = []
    for c_idx, computer in enumerate(computers):
        mem = []
        for n_idx, node in enumerate(computer):
            if node == 1 and not c_idx == n_idx: mem.append(n_idx)
        graph.append(mem)
    return graph

def solution(n, computers):
    graph = transper(computers)
    answer = 0
    visit = []

    for i in range(n):
        stack = [i]
        flag = False

        while stack:
            node = stack.pop()

            if node not in visit:
                flag = True
                visit.append(node)
                stack.extend(graph[node])

        if flag: answer += 1

    return answer
