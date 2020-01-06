def best_hands(hands):
    pass
    
# Development

def hand_rank(hand):
    hand = hand.replace("10", "T").split()
    card_ranks = ["..23456789TJQKA".index(r) for r, s in hand]
    groups = [(card_ranks.count(i), i) for i in set(card_ranks)]
    groups.sort(reverse=True)
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = (len(counts) == 5) and (max(ranks) - min(ranks) == 4)
    flush = len(set([s for r, s in hand])) == 1
    return (9 if counts == (5,) else
            8 if straight and flush else
            7 if counts == (4, 1) else
            6 if counts == (3, 2) else
            5 if flush else
            4 if straight else
            3 if counts == (3, 1, 1) else
            2 if counts == (2, 2, 1) else
            1 if counts == (2, 1, 1, 1) else
            0, ranks)

hand = "4S 5S 7H 8D JC"
print(hand)
hand = hand.replace("10", "T").split()
print(hand)
card_ranks = ["..23456789TJQKA".index(r) for r, s in hand]
print(card_ranks)
for r,s in hand:
    print(r,s)

