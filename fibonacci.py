mem = {}


def fibonacci_memoization(n):
    if n == 1 or n == 2:
        return 1

    if n in mem:
        return mem[n]
    else:
        mem[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return mem[n]


def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == '__main__':
    import time

    v = 50

    start_time = time.time()
    print(fibonacci_memoization(v))
    # print(fibonacci_recursive(v))
    print(time.time() - start_time)
