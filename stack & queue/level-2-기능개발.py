from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        sum = 0
        for index in range(len(progresses)):
            progresses[index] += speeds[index]
        
        try:
            while progresses[0] >= 100:
                sum += 1
                progresses.popleft()
                speeds.popleft()
        except: 
            answer.append(sum)
            break
        
        if sum != 0: answer.append(sum)
            
    return answer