num_computer = int(input())
num_network = int(input())

def generate_graph():
    graph = {}

    for _ in range(num_network):
        i, j = map(int, input().split())
        if i not in graph.keys(): graph[i] = []
        if j not in graph.keys(): graph[j] = []

        graph[i].append(j)
        graph[j].append(i)

    return graph

def dfs(graph):
    visited = []
    stack = [1]

    while stack:
        i = stack.pop()

        if i not in visited:
            visited.append(i)
            stack.extend(graph[i])

    return visited

print(len(dfs(generate_graph())) - 1 )