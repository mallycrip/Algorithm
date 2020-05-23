def solution(array, commands):
    answer = []
    for i in commands:
        j = array[i[0]-1:i[1]]
        j.sort()
        answer.append(j[i[2]-1])
    return answer
