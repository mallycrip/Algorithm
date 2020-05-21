import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    try:
        while heap[0] < K:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
            answer += 1
    except IndexError:
        answer = -1
        
    return answer