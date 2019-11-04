GIFTS = ['twelve Drummers Drumming',
         'eleven Pipers Piping',
         'ten Lords-a-Leaping',
         'nine Ladies Dancing',
         'eight Maids-a-Milking',
         'seven Swans-a-Swimming',
         'six Geese-a-Laying',
         'five Gold Rings',
         'four Calling Birds',
         'three French Hens',
         'two Turtle Doves',
         'a Partridge in a Pear Tree']

ORDINAL = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


day_number = 3
gifts = GIFTS[-day_number:]
if len(gifts) > 1:
    gifts[:-1] = [', '.join(gifts[:-1])]
print(gifts)
gifts = ', and '.join(gifts)
print(gifts)
# ~ print('On the {} day of Christmas my true love gave to me: {}.'.format(
        # ~ ORDINAL[day_number], gifts))
