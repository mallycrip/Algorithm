# 28776KB, 72ms
# DP Fibonacci 응용

mem = {0: (1, 0), 1: (0, 1)}


def fibonacci(n):
    if n in mem:
        return mem[n]
    else:
        minus_1 = fibonacci(n - 1)
        minus_2 = fibonacci(n - 2)
        mem[n] = (minus_1[0] + minus_2[0], minus_1[1] + minus_2[1])
        return mem[n]

    return mem[n]


if __name__ == '__main__':
    count = int(input())

    for _ in range(count):
        n = int(input())
        x, y = fibonacci(n)
        print(x, y)
