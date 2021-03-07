from datetime import datetime, timedelta

def gen_to_datetime(line):
    day, time, count = line.split(" ")
    end_time = datetime.fromisoformat(f"{day} {time}")
    start_time = end_time - timedelta(seconds=float(count.replace("s", "")) - 0.001)
    return start_time, end_time

def solution(lines):
    answer = 0
    graph = []
    for line in lines:
        graph.append(gen_to_datetime(line))

    for n in graph:
        s = 0
        e = 0
        for node in graph:
            start_1s = n[0] + timedelta(seconds=0.999)
            end_1s = n[1] + timedelta(seconds=0.999)

            if node[1] >= n[0] and node[0] <= start_1s:
                s += 1
            if node[1] >= n[1] and node[0] <= end_1s:
                e += 1

        answer = max(answer, s, e)

    return answer

if __name__ == '__main__':
    print(solution(
        ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
    ))