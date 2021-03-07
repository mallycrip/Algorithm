# Top-down으로 하니깐 시간초과 발생함
# Bottom-up은 잘됨 ㅇㅇ

import sys
sys.setrecursionlimit(10**7)

matrix = {}

def dp(n, money):
    global matrix
    if n < 0: return 0
    if n in matrix: return matrix[n]
    else:
        matrix[n] = max(dp(n - 2, money) + money[n], dp(n - 1, money))
        return matrix[n]

def solution(money):
    if len(money) == 1: return money[0]
    global matrix

    dp_1 = dp(len(money) - 2, money[1:])


    print(matrix)
    matrix = {}
    dp_2 = dp(len(money) - 2, money)

    print(matrix)
    return max(dp_1, dp_2)

if __name__ == '__main__':
    solution([1,4,2,4,1,6,7,6,4,3,6,5,4])

# def solution(money):
#     matrix_1 = [money[0], money[0]]
#     for n in range(2, len(money) - 1):
#         matrix_1.append(max(money[n] + matrix_1[n - 2], matrix_1[n - 1]))
#
#     matrix_2 = [0, money[1]]
#     for n in range(2, len(money)):
#         matrix_2.append(max(money[n] + matrix_2[n - 2], matrix_2[n - 1]))
#
#     return max(matrix_1[-1], matrix_2[-1])
