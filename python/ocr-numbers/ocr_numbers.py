DIGIT_WIDTH = 3
DIGIT_HEIGHT = 4

NUMS = {
    ' _ | ||_|   ': '0',
    '     |  |   ': '1',
    ' _  _||_    ': '2',
    ' _  _| _|   ': '3',
    '   |_|  |   ': '4',
    ' _ |_  _|   ': '5',
    ' _ |_ |_|   ': '6',
    ' _   |  |   ': '7',
    ' _ |_||_|   ': '8',
    ' _ |_| _|   ': '9'
}


def convert(input_grid):
    if len(input_grid) % DIGIT_HEIGHT != 0 \
       or len(input_grid[0]) % DIGIT_WIDTH != 0:
        raise ValueError("Invalid input grid")
    response = ""
    for k in range(0, len(input_grid), DIGIT_HEIGHT):
        if len(response) > 2:
            response += ","
        for j in range(0, len(input_grid[0]), DIGIT_WIDTH):
            one_liner = ''
            for i in range(DIGIT_HEIGHT):
                one_liner += input_grid[k+i][j:j+DIGIT_WIDTH]
            if one_liner in NUMS.keys():
                response += NUMS[one_liner]
            else:
                response += "?"
    return response
