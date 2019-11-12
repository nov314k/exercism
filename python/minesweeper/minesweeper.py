VALID_CHARS = [' ', '*']


def annotate(minefield):
    if minefield == []:
        return []
    if not is_valid(minefield):
        raise ValueError("Minefield is not valid")
    board = []
    blank_row = ' '.join('' for i in range(len(minefield[0]) + 3))
    board.append(blank_row)
    for row in minefield:
        board.append(' ' + row + ' ')
    board.append(blank_row)
    result = []
    for i in range(1, len(board) - 1):
        new_row = ""
        for j in range(1, len(board[0]) - 1):
            if board[i][j] == '*':
                new_row += '*'
            else:
                counter = 0
                for m in [-1, +1]:
                    # Rows above and below
                    counter += board[i + m][j - 1:j + 2].count('*')
                    # Characters to the left and right
                    counter += board[i][j + m].count('*')
                if counter == 0:
                    new_row += board[i][j]
                else:
                    new_row += str(counter)
        result.append(new_row)
    return result


def is_valid(minefield):
    valid_length = len(minefield[0])
    for row in minefield:
        if len(row) != valid_length:
            return False
        for char in row:
            if char not in VALID_CHARS:
                return False
    return True
