mem = {1: 1, 2: 3}

def solution_1(n):
    if n in mem: return mem[n]
    else:
        mem[n] = solution_1(n - 1) + solution_1(n - 2) + solution_1(n - 2)
        return mem[n]

if __name__ == '__main__':
    print(solution_1(30))
