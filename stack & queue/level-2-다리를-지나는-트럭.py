from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*(bridge_length))
    truck_weights = deque(truck_weights)
    answer = 0
    sum = 0

    while truck_weights:
        bridge.append(truck_weights[0])
        sum -= bridge.popleft()
        sum += truck_weights[0]

        if sum > weight:
            bridge.pop()
            bridge.append(0)
            sum -= truck_weights[0]
        else: truck_weights.popleft()
        answer += 1
    answer += bridge_length


    return answer
