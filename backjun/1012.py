def generate_graph(_map):
    graph = {}

    for y, x_list in enumerate(_map):
        for x, element in enumerate(x_list):
            if element == 1:
                idx = len(x_list) * y + x
                if idx not in graph:
                    graph[idx] = []

                if find_top(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx - len(x_list))
                if find_bottom(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx + len(x_list))
                if find_left(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx - 1)
                if find_right(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx + 1)

    return graph


def find_top(_map, max_of_x, x, max_of_y, y):
    if y == 0: return False
    if _map[y - 1][x] == 1: return True
    return False


def find_bottom(_map, max_of_x, x, max_of_y, y):
    if y == max_of_y: return False
    if _map[y + 1][x] == 1: return True
    return False


def find_left(_map, max_of_x, x, max_of_y, y):
    if x == 0: return False
    if _map[y][x - 1] == 1: return True
    return False


def find_right(_map, max_of_x, x, max_of_y, y):
    if x == max_of_x: return False
    if _map[y][x + 1] == 1: return True
    return False


def generate_map(max_of_x, max_of_y, num_of_cabbages):
    _map = [[0 for _ in range(max_of_x)] for _ in range(max_of_y)]

    for _ in range(num_of_cabbages):
        x, y = map(int, input().split())
        _map[y][x] = 1

    return _map

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
    x, y, num_of_cabbages = map(int, input().split())

    _visited = []
    answer = 0
    graph = generate_graph(generate_map(x, y, num_of_cabbages))

    for i in graph.keys():
        if i not in _visited:
            answer += 1
            _visited.extend(dfs(graph, i))

    return answer


if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        print(solution())
