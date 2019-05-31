def on_square(square):
    check_input(square)
    return 2 ** (square - 1)


def total_after(square):
    check_input(square)
    return sum(
        on_square(n + 1)
        for n in range(square))


def check_input(square):
    if square == 0 or square < 0 or square > 64:
        raise ValueError("Invalid input")
