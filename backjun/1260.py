# 29680KB, 728ms
# 머리속에 있는대로 짜서 코드 퀄리티가 좋지 못함
# 어떤 사람들은 72ms가 나오던데 어떻게 한거지 ㅋㅋ

nodes, lines, start = map(int, input().split())

graph = {}

for node in range(1, nodes + 1):
    graph[node] = []

for _ in range(lines):
    n1, n2 = map(int, input().split())

    graph[n1].append(n2)
    graph[n2].append(n1)


def dfs():
    visited = []
    stack = [start]

    while stack:
        i = stack.pop()
        if i not in visited:
            stack.extend(sorted(graph[i], reverse=True))
            visited.append(i)

    return visited


def bfs():
    visited = []
    queue = [start]

    while queue:
        i = queue.pop(0)
        if i not in visited:
            queue.extend(sorted(graph[i]))
            visited.append(i)

    return visited


print(" ".join(map(str, dfs())))
print(" ".join(map(str, bfs())))
