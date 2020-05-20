import copy
from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    answer = 0
    while location > -1:
        priorities_copy = copy.deepcopy(priorities)
        priorities_copy = sorted(priorities_copy, reverse=True)

        print(priorities, priorities_copy, location, answer)

        if priorities[0] >= priorities_copy[0]:
            priorities.popleft()
            location -= 1
            answer += 1
        else:
            priorities.append(priorities.popleft())
            if location == 0: location = len(priorities)
            location -= 1

    return answer