def verify(isbn):
    if len(isbn) == 0:
        return False
    core_isbn = isbn[:len(isbn)-1]
    check_digit = isbn[-1]
    digital_isbn = ''
    for c in core_isbn:
        if c.isdigit():
            digital_isbn += c
    if len(digital_isbn) != 9:
        return False
    coeffs = reversed(range(1, 10))
    sum = 0
    for c in coeffs:
        sum += int(digital_isbn[c-1]) * c
    if check_digit.isdigit():
        sum += int(check_digit) * 10
    elif check_digit == 'X':
        sum += 10 * 10
    else:
        return False
    if sum % 11 == 0:
        return True
    else:
        return False
