def sum_of_multiples(limit, multiples):
    factors = [i for i in range(limit)
               if any(i % j == 0 for j in multiples if j > 0)]
    return sum(factors)
