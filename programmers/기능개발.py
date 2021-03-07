from collections import deque


def get_day(progress, speed):
    day = (100 - progress) // speed
    if (100 - progress) % speed != 0:
        return day + 1
    else:
        return day


def solution(progresses, speeds):
    answer = []
    queue = deque([])

    for progress, speed in zip(progresses, speeds):
        queue.append(get_day(progress, speed))

    while queue:
        ans = 1
        i = queue.popleft()
        while len(queue) != 0 and i >= queue[0]:
            queue.popleft()
            ans += 1
        answer.append(ans)

    return answer


if __name__ == '__main__':
    print(solution([99, 1, 99, 1], [1,1,1,1]))