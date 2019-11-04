def is_paired(input_string):
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for c in input_string:
        if c in matching_brackets.values():
            stack.append(c)
        elif c in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[c]:
                return False
            stack.pop()
    return not stack

