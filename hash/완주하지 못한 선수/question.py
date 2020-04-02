def solution(participant, completion):
    for _participant, _completion in zip(sorted(participant), sorted(completion)):
        if _participant != _completion: return _participant

    return participant[-1]


# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]