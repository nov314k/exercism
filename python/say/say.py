NUMBERS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion',
}

MIN_NUMBER = 0
MAX_NUMBER = 999999999999
LOWER_MAGNITUDES = [1e2, 1e1]
HIGHER_MAGNITUDES = [1e9, 1e6, 1e3]


def hundreds_tens_ones(number):
    in_words = ''
    while number >= 20:
        for order in LOWER_MAGNITUDES:
            intquo = number // order
            if intquo > 0:
                if order == 1e1 and number >= 20:
                    in_words += NUMBERS[intquo * order]
                else:
                    in_words += NUMBERS[intquo] + ' ' + NUMBERS[order]
                if number % order != 0:
                    if order == 10:
                        in_words += '-'
                    elif order == 100:
                        in_words += ' and '
                    else:
                        in_words += ' '
                number -= intquo * order
    if number > 0:
        in_words += NUMBERS[number]
    return in_words


def say(number):
    in_words = ''
    if number < MIN_NUMBER or number > MAX_NUMBER:
        raise ValueError('Number is outside the valid range!')
    if number == 0:
        return NUMBERS[number]
    for order in HIGHER_MAGNITUDES:
        intquo = number // order
        if intquo > 0:
            in_words += hundreds_tens_ones(intquo) + ' ' + NUMBERS[order]
            if number % order != 0:
                in_words += ' '
            number -= intquo * order

    return in_words + hundreds_tens_ones(number)
