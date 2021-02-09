mem = {0: 0}


def cut_rod(price, n):
    if n in mem:
        return mem[n]
    else:
        max_num = price[n - 1]
        for i in range(1, n):
            max_num = max(max_num, cut_rod(price, n - i) + cut_rod(price, i))
        mem[n] = max_num
        return mem[n]


if __name__ == '__main__':
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(price)

    print(cut_rod(price, size))
