# 28776KB 64ms

mem = {0: 0, 1: 1}


def fibonacci(n):
    if n in mem:
        return mem[n]
    else:
        mem[n] = fibonacci(n - 2) + fibonacci(n - 1)
        return mem[n]


if __name__ == '__main__':
    print(fibonacci(int(input())))
