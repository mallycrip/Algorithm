mem = {1: [[1]],
       2: [[2], [1, 1]]}


def solution_2(n):
    if n in mem: return mem[n]
    else:
        mem[n] = []
        mem[n].append([n])
        for i in range(1, n):
            l = []
            if i > n - i:
                break
            n1 = solution_2(n - i)
            m1 = solution_2(i)
            for x in n1:
                for y in m1:
                    if any(x[0] < y1 for y1 in y):
                        break
                    l.append(sorted(x + y, reverse=True))
            mem[n].extend(l)

    return mem[n]


if __name__ == '__main__':
    ans = solution_2(15)
    i = []
    for j in ans:
        if not j in i: i.append(j)

    for j in sorted(i, reverse=True):
        print(' '.join(map(str, j)))

    print(f"경우의 수 : {len(i)}")
