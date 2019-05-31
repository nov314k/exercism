def steps(number):
    if number <= 0:
        raise ValueError("Number cannot be zero!")
    numof_steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        numof_steps += 1
    return numof_steps
