pan_gramma = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(sentence):
    # '>' is crucial here, to capture all non-alpha characters in sentence
    return set(list(sentence.lower())) >= set(list(pan_gramma.lower()))
