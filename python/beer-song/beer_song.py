def recite(start, take=1):
    results = []
    for i in range(start, start - take, -1):
        results.extend(first_line(i))
        if i > start - take + 1:
            results.append('')
    return results


def first_line(number):
    return [
        ''.join([
            "{} of beer on the wall, ".format(bottles(number).capitalize()),
            "{} of beer.".format(bottles(number))
        ]),
        ''.join([
            second_line(number),
            next_bottle(number)
        ])
    ]


def second_line(current_verse):
    if current_verse == 0:
        return "Go to the store and buy some more, "
    else:
        return "Take {} down and pass it around, ".format(
            "one" if current_verse > 1 else "it",
        )


def next_bottle(current_verse):
    return "{} of beer on the wall.".format(
        bottles(next_verse(current_verse)),
    )


def bottles(number):
    if number == 0:
        return 'no more bottles'
    if number == 1:
        return '1 bottle'
    else:
        return '{} bottles'.format(number)


def next_verse(current_verse):
    return current_verse - 1 if current_verse > 0 else 99
