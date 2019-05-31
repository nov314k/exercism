def classify(number):
    if number < 1:
        raise ValueError("Invalid input")
    s = sum([i for i in range(1, number-1) if number % i == 0])
    if s == number:
        return "perfect"
    elif s > number:
        return "abundant"
    else:
        return "deficient"
