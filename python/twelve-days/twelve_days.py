GIFTS = ["twelve Drummers Drumming",
         "eleven Pipers Piping",
         "ten Lords-a-Leaping",
         "nine Ladies Dancing",
         "eight Maids-a-Milking",
         "seven Swans-a-Swimming",
         "six Geese-a-Laying",
         "five Gold Rings",
         "four Calling Birds",
         "three French Hens",
         "two Turtle Doves",
         "a Partridge in a Pear Tree."]


DAYS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "twelfth"]


def _enumerate_phrases(phrases):
    *phrases, last_phrase = phrases
    if not phrases:
        return last_phrase
    return f'{", ".join(phrases)}, and {last_phrase}'


def _recite_verse(verse):
    stanza = _enumerate_phrases(GIFTS[-verse:])
    return f"On the {DAYS[verse-1]} day of Christmas " \
           f"my true love gave to me: {stanza}"


def recite(start_verse, end_verse):
    return [_recite_verse(n) for n in range(start_verse, end_verse+1)]
