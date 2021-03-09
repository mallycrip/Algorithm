import heapq
from collections import deque


def solution(operations):
    operations = deque(operations)
    heap = []
    while operations:
        i = operations.popleft()
        if i[0] == "I":
            _, v = i.split(" ")
            heapq.heappush(heap, int(v))
        elif heap:
            if i == "D 1":
                heapq._heapify_max(heap)
                heapq.heappop(heap)
            else:
                heapq.heapify(heap)
                heapq.heappop(heap)

    if heap:
        heapq.heapify(heap)
        x = heapq.heappop(heap)
        if heap:
            heapq._heapify_max(heap)
            y = heapq.heappop(heap)
        else:
            y = x
    else:
        x = y = 0

    return [y, x]

if __name__ == '__main__':
    print(solution(["I 7","I 5","I -5","D -1"]))