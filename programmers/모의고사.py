first = [1, 2, 3, 4, 5]
second = [2, 1, 2, 3, 2, 4, 2, 5]
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def compare(list_1, list_2):
    return len([i for i, j in zip(list_1, list_2) if i == j])


def marking(answers, list):
    right = 0
    for i in range(len(answers) // len(list) + 1):
        right += compare(answers[i * len(list): len(list) * (i + 1)], list)

    return right


def solution(answers):
    answer = []

    first_answer = marking(answers, first)
    second_answer = marking(answers, second)
    third_answer = marking(answers, third)

    max_answer = max(first_answer, second_answer, third_answer)

    if first_answer == max_answer: answer.append(1)
    if second_answer == max_answer: answer.append(2)
    if third_answer == max_answer: answer.append(3)

    return answer
