import sys
from operator import add, mul, sub, floordiv as div

OPERATIONS = {
    'plus': add,
    'minus': sub,
    'multiplied by': mul,
    'divided by': div
}


def answer(question):
    words = question[8:-1].strip().lower().split()
    if not words:
        raise ValueError("Invalid question")
    words.reverse()
    last_value = int(words.pop())
    while words:
        operations = [words.pop()]
        while words:
            try:
                next_to_evaluate = words.pop()
                second_value = int(next_to_evaluate)
                break
            except ValueError:
                operations.append(next_to_evaluate)
        else:
            raise ValueError("Invalid question")
        operations = ' '.join(operations)
        try:
            last_value = OPERATIONS[operations](last_value, second_value)
        except KeyError:
            raise ValueError("Invalid question")
    return last_value
