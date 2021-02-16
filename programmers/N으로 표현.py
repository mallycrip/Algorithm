mem = []

def solution(N, number):
    answer = -1

    for i in range(1, 9):  # -> 1 ~ 8
        n = [int(str(N) * i)]
        for j, m in enumerate(mem):
            for y in mem[i - j - 2]:
                for x in m:
                    n.append(x + y)
                    n.append(x - y)
                    n.append(x * y)
                    if y != 0: n.append(x // y)

        n = set(n)

        if number in n:
            return i

        mem.append(n)

    return answer
