def is_vps(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(True)
        elif i == ")":
             stack.pop()

    if stack: return False
    return True

def solution():
