
def generate_graph(lines):
    graph = {}

    for _ in range(lines):
        u, v = map(int, input().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

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


def solution():
    nodes, lines = map(int, input().split())
    visited = []
    answer = 0
    graph = generate_graph(lines)

    for i in range(1, nodes + 1):
        if i not in visited:
            if i in graph: visited.extend(dfs(graph, i))
            answer += 1

    return answer


print(solution())
