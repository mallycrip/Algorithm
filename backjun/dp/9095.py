# 28776KB 64ms

mem = {1: 1, 2: 2, 3: 4}


def solution(n):
    if n in mem:
        return mem[n]
    else:
        mem[n] = solution(n - 3) + solution(n - 2) + solution(n - 1)
        return mem[n]


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(solution(int(input())))
