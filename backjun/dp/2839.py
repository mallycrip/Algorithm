# 29540KB, 72ms
# 재귀에 대한 부분이 너무 약해서 이번 문제는 가능한 재귀로 풀어보려고 하였다.
# DP중 기초에 해당하는 것 같다. 

import sys
sys.setrecursionlimit(10**7)

i = int(input())

mem = [-1 for _ in range(i)]

if i >= 3: mem[2] = 1
if i >= 5: mem[4] = 1

def solution(n):
    if n <= 0: return -1
    if mem[n - 1] != -1:
        return mem[n - 1]
    else:
        min_value_five = solution(n - 5)
        min_value_three = solution(n - 3)
        if min_value_five != -1 and min_value_three != -1:
            mem[n - 1] = min_value_five + 1 if min_value_five < min_value_three else min_value_three + 1
        elif min_value_five != -1: mem[n - 1] = min_value_five + 1
        elif min_value_three != -1: mem[n - 1] = min_value_three + 1

        return mem[n - 1]

print(solution(i))