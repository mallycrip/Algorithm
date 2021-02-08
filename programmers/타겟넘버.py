def bf(numbers, target):
    print(numbers, end=" ")
    if len(numbers) == 1:
        if numbers[0] == target: return 1
        else: return 0

    plus_numbers = numbers[:]
    plus_numbers[1] = numbers[0] + numbers[1]
    minus_numbers = numbers[:]
    minus_numbers[1] = numbers[0] - numbers[1]

    return bf(plus_numbers[1:], target) + bf(minus_numbers[1:], target)


def solution(numbers, target):
    numbers.insert(0, 0)
    return bf(numbers, target)

numbers = [1, 1, 1, 1, 1]

target =3

print(solution(numbers, target))