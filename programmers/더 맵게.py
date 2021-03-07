import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    i = heapq.heappop(scoville)
    answer = 0
    while i < K:
        if len(scoville) == 0: return -1
        j = heapq.heappop(scoville)
        heapq.heappush(scoville, i + (j * 2))
        i = heapq.heappop(scoville)
        answer += 1

    return answer

print(solution([0, 1, 5], 5))