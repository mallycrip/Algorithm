def bfs(start_node, graph):
    visit = []
    queue = [start_node]

    while queue:
        n = queue.pop(0)
        if n not in visit:
            visit.append(n)
            queue.extend(graph[n])

    print(visit)

graph = {
    "A": ["B", "C", "D"],
    "B": ["A"],
    "C": ["A"],
    "D": ["A"]
}

if __name__ == '__main__':
    bfs("A", graph)