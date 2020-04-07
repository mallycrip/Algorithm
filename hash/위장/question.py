def solution(clothes):
    a_dict = {}
    answer = 0
    for c, c_type in clothes:
        if c_type in a_dict.keys():
            a_dict[c_type].append(c)
        else:
            a_dict[c_type] = [c]

    for v in a_dict.values():
        answer += len(v) + 1
    answer = answer - 1
    return answer


# 프로그래머스 답안
# def solution(clothes):
# from collections import Counter
# from functools import reduce
# cnt = Counter([kind for name, kind in clothes])
# answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
# return answer
