mem = {}


def fibonacci_memoization(n):
    if n == 1 or n == 2:
        return 1

    if n in mem:
        return mem[n]
    else:
        mem[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return mem[n]
