def solution(s):
    length = len(s)
    max = length

    for i in range(1, length):
        start = 0
        end = i
        foo = ""
        bar = 0
        count = 1
        saveList = []
        flag = False

        for _ in range(length - i + 1):
            sli = s[start:end]
            saveList.append(sli)
            start += i
            end += i

        for str in saveList:
            if not foo:
                foo = str
                bar += len(str)

            elif str == foo:
                if not flag:
                    bar += 1
                    count += 1
                    flag = True
                else: count += 1

            else:
                foo = str
                count = 1
                bar += len(str)
                flag = False

            if count == 10: bar += 1
            elif count == 100: bar += 1
            elif count == 1000: bar += 1

        if max > bar: max = bar

    return max


if __name__ == '__main__':
    iString = input()
    print(solution(iString))