import heapq


def solution(stock, dates, supplies, k):
    heap = []
    answer = 0
    index = 0
    while stock < k:
        for i in range(index, len(dates)):
            if dates[i] > stock:
                break
            heapq.heappush(heap, -supplies[i])
            index += 1
        stock += heapq.heappop(heap) * -1
        answer += 1

    return answer