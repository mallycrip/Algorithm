# 53468KB, 292ms

matrix = []
mem = {}

def generate_matrix(n):
    for _ in range(n):
        i = list(map(int, input().split()))
        matrix.append(i)

    mem[(0, 0)] = matrix[0][0]


def triangle(idx):
    if idx in mem:
        return mem[idx]
    else:
        if idx[1] == 0:
            mem[idx] = triangle((idx[0] - 1, idx[1])) + matrix[idx[0]][idx[1]]
            return mem[idx]
        elif idx[1] == len(matrix[idx[0]]) - 1:
            mem[idx] = triangle((idx[0] - 1, idx[1] - 1)) + matrix[idx[0]][idx[1]]
            return mem[idx]

        left = triangle((idx[0] - 1, idx[1] - 1))
        right = triangle((idx[0] - 1, idx[1]))
        mem[idx] = left + matrix[idx[0]][idx[1]] if left > right else right + matrix[idx[0]][idx[1]]

        return mem[idx]


if __name__ == '__main__':
    n = int(input())
    generate_matrix(n)

    max = 0
    for i in range(n):
        v = triangle((n - 1, i))
        if v > max: max = v

    print(max)
