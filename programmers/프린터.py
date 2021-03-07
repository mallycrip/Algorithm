from collections import deque


def check_queue(queue, i):
    for j in queue:
        if j > i:
            return False
            break
    return True


def solution(priorities, location):
    queue = deque(priorities)
    answer = []

    while location != -1:
        print(queue, location, answer)
        location -= 1
        i = queue.popleft()
        if location == -1:
            if not check_queue(queue, i):
                location = len(queue)
                queue.append(i)
            else:
                answer.append(i)
        else:
            if not check_queue(queue, i):
                queue.append(i)
            else:
                answer.append(i)
    return len(answer)

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))