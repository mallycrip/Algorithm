def generate_graph(begin, words):
    graph = {}
    words.append(begin)
    for idx, word in enumerate(words):
        graph[word] = []
        for compare_word in words:
            if len([None for w, c in zip(word, compare_word) if w != c]) == 1:
                graph[word].append(compare_word)

    return graph


def bfs(graph, start_node, target):
    visited = []
    queue = [start_node]
    depth = 0
    next_queue = []

    while queue:
        i = queue.pop(0)
        if i == target: return depth
        if i not in visited:
            visited.append(i)
            next_queue.extend(graph[i])

        if not queue:
            queue.extend(next_queue)
            next_queue = []
            depth += 1

    return 0


def solution(begin, target, words):
    return bfs(generate_graph(begin, words), begin, target)


print(solution("hit", "cog", ["dot", "dog", "lot", "log", "cog"]))