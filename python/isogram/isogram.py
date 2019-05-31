def is_isogram(string):
    processed = string.replace(" ", "").replace("-", "").lower()
    if len(processed) == len(set(processed)):
        return True
    return False
