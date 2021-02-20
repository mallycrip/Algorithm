# set에 대해서 다시 생각하게 된 문제

def gen_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

def bfs(start_node, graph):
    visited = set()
    queue = []
    mem = [start_node]
    answer_mem = []

    while mem:
        queue.extend(mem)
        mem = []
        answer = []
        while queue:
            i = queue.pop(0)

            if i not in visited:
                visited.add(i)
                answer.append(i)
                mem.extend(graph[i])

        mem = list(set(mem))
        answer_mem.append(answer)

    return answer_mem[-2]


def solution(n, edge):
    return len(bfs(1, gen_graph(n, edge)))


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
