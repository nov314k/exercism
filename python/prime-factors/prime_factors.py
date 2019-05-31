def prime_factors(natural_number):
    factors = []
    divisor = 2
    while natural_number > 1:
        while natural_number % divisor == 0:
            factors.append(divisor)
            natural_number /= divisor
        divisor += 1
    return factors
