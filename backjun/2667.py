# 28776KB 76ms

def generate_map(size):
    _map = []
    for _ in range(size):
        _map.append(list(input()))
    return _map


def generate_graph(_map):
    graph = {}

    for y, _x in enumerate(_map):
        for x, i in enumerate(_x):
            if i == "1":
                idx = ((y) * len(_map)) + (x + 1)
                graph[idx] = []

                if search_top(_map, y, x): graph[idx].append(idx - len(_map))
                if search_bottom(_map, y, x): graph[idx].append(idx + len(_map))
                if search_left(_map, y, x): graph[idx].append(idx - 1)
                if search_right(_map, y, x): graph[idx].append(idx + 1)

    return graph


def search_top(_map, current_y, currnet_x):
    if current_y == 0: return False
    if _map[current_y - 1][currnet_x] == "1": return True
    return False


def search_bottom(_map, current_y, currnet_x):
    if current_y == len(_map) - 1: return False
    if _map[current_y + 1][currnet_x] == "1": return True
    return False


def search_left(_map, current_y, currnet_x):
    if currnet_x == 0: return False
    if _map[current_y][currnet_x - 1] == "1": return True
    return False


def search_right(_map, current_y, currnet_x):
    if currnet_x == len(_map) - 1: return False
    if _map[current_y][currnet_x + 1] == "1": return True
    return False


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        i = stack.pop()
        if i not in visited:
            stack.extend(graph[i])
            visited.append(i)

    return len(visited), visited


def solution(graph):
    _visited = []
    _sizes = []
    for key in graph.keys():
        if key not in _visited:
            size, visited = dfs(graph, key)
            _visited.extend(visited)
            _sizes.append(size)

    _sizes.sort()
    print(len(_sizes))
    for size in _sizes:
        print(size)


solution(generate_graph(generate_map(int(input()))))
