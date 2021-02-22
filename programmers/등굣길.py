# 엄청 쉽게 푼 문제

matrix = list()

def generate_matrix(m, n, puddles):
    global matrix
    matrix = [
        [-1 if i != 0 else None for i in range(m + 1)] if j != 0 else [None for _ in range(m + 1)]
        for j in range(n + 1)
    ]

    for puddle in puddles:
        matrix[puddle[1]][puddle[0]] = None

    matrix[1][1] = 1

def dp(m, n):
    global matrix
    if not matrix[n][m]: return 0
    if matrix[n][m] != -1: return matrix[n][m]
    else:
        matrix[n][m] = dp(m - 1, n) + dp(m, n - 1)
        return matrix[n][m]


def solution(m, n, puddles):
    generate_matrix(m, n, puddles)
    return dp(m, n) % 1000000007
