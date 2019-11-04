import re

VALID_PATTERN = re.compile("[a-z0-9]+(['][a-z]+)?")


def count_words(text):
    catalog = dict()
    words = [word.group(0) for word in VALID_PATTERN.finditer(text.lower())]
    for word in words:
        if word in catalog.keys():
            catalog[word] += 1
        else:
            catalog[word] = 1
    return catalog
