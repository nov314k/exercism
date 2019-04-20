def is_armstrong(number):
    sum_of_digits = 0
    for n in str(number):
        sum_of_digits += int(n) ** len(str(number))
    return number == sum_of_digits
