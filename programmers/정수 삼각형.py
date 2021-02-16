mem = {}
triangle = []


def dp(idx):
    if idx in mem:
        return mem[idx]
    else:
        if idx[1] == 0:
            mem[idx] = dp((idx[0] - 1, idx[1])) + triangle[idx[0]][idx[1]]
            return mem[idx]
        if idx[1] == len(triangle[idx[0]]) - 1:
            mem[idx] = dp((idx[0] - 1, idx[1] - 1)) + triangle[idx[0]][idx[1]]
            return mem[idx]

        mem[idx] = max(dp((idx[0] - 1, idx[1])) + triangle[idx[0]][idx[1]], dp((idx[0] - 1, idx[1] - 1)) + triangle[idx[0]][idx[1]])
        return mem[idx]


def solution(_triangle):
    global triangle
    triangle = _triangle
    mem[(0, 0)] = triangle[0][0]

    answer = 0

    for i in range(len(triangle)):
        answer = max(answer, dp((len(triangle) - 1, i)))

    return answer

if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
