def generate_graph(computers):
    graph = []

    for computer, nodes in enumerate(computers):
        graph.append([i for i, x in enumerate(nodes) if x == 1 and not computer == i])

    return graph

def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        i = stack.pop()
        if i not in visited:
            visited.append(i)
            stack.extend(graph[i])

    return visited



def solution(n, computers):
    answer = 0
    visited = []
    graph = generate_graph(computers)

    for computer in range(n):
        if computer not in visited:
            visited.extend(dfs(graph, computer))
            answer += 1


    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))