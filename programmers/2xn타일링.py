import sys
sys.setrecursionlimit(10**9)

mem = {}

def dp(n):
    if n in mem: return mem[n]
    else:
        mem[n] = dp(n - 1) + dp(n - 2)
        return mem[n]

def solution(n):
    global mem
    mem[1] = 1
    mem[2] = 2
    return dp(n)

if __name__ == '__main__':
    print(solution(int(input())))
    print(mem)