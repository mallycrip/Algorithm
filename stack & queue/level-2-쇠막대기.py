def solution(arrangement):
    stack = []
    answer = 0
    for index, i in enumerate(arrangement):
        try:
            if str(i) + str(arrangement[index+1]) == "()":
                answer += len(stack)
            else:
                if str(i) == ")": 
                    if str(arrangement[index-1]) + str(i) == "()": pass
                    else: stack.pop()
                else: 
                    stack.append("(")
                    answer += 1
        except:
            pass
    return answer