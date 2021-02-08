# PyPy3 : 125,488KB, 224ms
# Python3 : 31,624KB, 3216ms
# 시간복잡도가 큰거 같다 조금 더 효율적인 방법이 있는 듯
# 가장 전형적인 BFS문제이다. 짧은 거리 구하기 인데, 도착 지점까지의 Depth가 최단 거리이므로 BFS를 응용하여 풀면 된다.
# 그래프 문제중에서 2차원배열을 이용한 문제가 많다. 지금까지 위아래양옆을 확인하는 함수를 사용하였는데 비효율적인듯하다.
# 나는 문제를 대부분 딕셔너리 형태를 이용하는데 다른 사람들 풀이를 보면 2차원배열에서 바꿔가면서 사용한다. 그 방법에 익숙해져야할듯.


def generate_map(y):
    _map = []
    for _ in range(y):
        x = list(input())
        _map.append(x)

    return _map


def generate_graph(_map):
    graph = {}

    for y, x_list in enumerate(_map):
        for x, element in enumerate(x_list):
            if element == "1":
                idx = y * len(x_list) + x
                graph[idx] = []
                if check_top(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx - len(x_list))
                if check_bottom(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx + len(x_list))
                if check_left(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx - 1)
                if check_right(_map, len(x_list) - 1, x, len(_map) - 1, y): graph[idx].append(idx + 1)


    return graph


def check_top(_map, max_of_x, x, max_of_y, y):
    if y == 0: return False
    elif _map[y - 1][x] == "1": return True
    else: return False


def check_bottom(_map, max_of_x, x, max_of_y, y):
    if y == max_of_y: return False
    elif _map[y + 1][x] == "1": return True
    else: return False


def check_left(_map, max_of_x, x, max_of_y, y):
    if x == 0: return False
    elif _map[y][x - 1] == "1": return True
    else: return False


def check_right(_map, max_of_x, x, max_of_y, y):
    if x == max_of_x: return False
    elif _map[y][x + 1] == "1": return True
    else: return False


def bfs(graph, start_node, end_node):
    visited = [start_node]
    queue = []
    depth_mem = []
    depth = 1

    depth_mem.extend(graph[start_node])

    while depth_mem:
        depth += 1
        queue.extend(depth_mem)
        depth_mem = []
        while queue:
            i = queue.pop(0)
            if i == end_node: return depth
            if i not in visited:
                visited.append(i)
                depth_mem.extend(graph[i])

    return depth


if __name__ == '__main__':
    y, x = map(int, input().split())
    print(bfs(generate_graph(generate_map(y)), 0, x * y - 1))
