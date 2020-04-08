def solution(genres, plays):
    answer = []
    key_order = []
    foo = {}
    zipped = zip(genres, plays, range(len(genres)))

    for i in zipped:
        if i[0] in foo.keys(): foo[i[0]].append((i[1], i[2]))
        else: foo[i[0]] = [(i[1], i[2])]

    for i in foo.keys():
        foo[i].sort(key = lambda x: (-x[0] ,x[1]))

    for i in foo.keys():
        sum = 0
        for j in foo[i]:
            sum += j[0]
        key_order.append((i, sum))

    key_order.sort(key = lambda x: -x[1])

    for key, _ in key_order:
        answer.append(foo[key][0][1])
        try: answer.append(foo[key][1][1])
        except: pass

    return answer