def solution(n):
    stack = [n]
    while stack[-1] > 3:
        i = stack.pop()
        stack.append(i % 3)
        stack.append((i - 1) // 3)

    print(stack)

    return "".join(["4" if x == 3 or x == 0 else str(x) for x in reversed(stack)])

print(solution(10))