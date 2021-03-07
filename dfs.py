def dfs(start_node, graph):
    visit = []
    stack = [start_node]

    while stack:
        n = stack.pop(0)
        if n not in visit:
            visit.append(n)
            stack.extend(graph[n])

    print(visit)

graph = {
    "A": ["B", "C", "D"],
    "B": ["A"],
    "C": ["A"],
    "D": ["A"]
}

if __name__ == '__main__':
    dfs("A", graph)