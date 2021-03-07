def union(stack, i, j):
    j_value = stack[j]
    stack[j] = stack[i]

    while j_value in stack:
        stack[stack.index(j_value)] = stack[i]

    return stack


def check_cycle(stack, i, j):
    return stack[i] == stack[j]


def solution(n, costs):
    stack = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2], reverse=True)
    answer = 0
    bridge = 0

    while bridge < n - 1:
        i, j, v = costs.pop()
        if not check_cycle(stack, i, j):
            stack = union(stack, i, j)
            answer += v
            bridge += 1

    return answer

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))