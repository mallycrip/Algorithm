import heapq
from collections import deque


def solution(routes):
    routes = deque(sorted(routes))
    heap = []
    answer = 0
    idx = routes[0][0]
    while routes:
        next_idx = routes[0][0]
        if heap and heap[0][0] < idx:
            heap = []
            answer += 1
        if routes[0][0] == idx:
            i = routes.popleft()
            heapq.heappush(heap, [i[1], i[0]])
        idx = next_idx

    return answer + 1


if __name__ == '__main__':
    print(solution([[0, 0], [0, 0]]))
