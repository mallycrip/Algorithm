# 실패. 시간 제한 걸림. 

import sys
input = sys.stdin.readline

def generate_graph(computers, lines):
    graph = [[] for _ in range(computers)]

    for _ in range(lines):
        a, b = map(int, input().split())
        graph[b - 1].append(a - 1)

    return graph


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        i = stack.pop()
        if i not in stack:
            visited.append(i)
            stack.extend(graph[i])

    return visited


def solution(computers, lines):
    answer = []
    max = 0

    graph = generate_graph(computers, lines)

    for computer in range(computers):
        if graph[computer]:
            value = len(dfs(graph, computer))

            if max < value:
                answer = [computer + 1]
                max = value

            elif max == value:
                answer.append(computer + 1)

    return answer


if __name__ == '__main__':
    computers, lines = map(int, input().split())
    print(*solution(computers, lines))
