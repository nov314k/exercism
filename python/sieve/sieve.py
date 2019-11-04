def primes(limit):
    marked = []
    primes = []
    for i in range(2, limit+1):
        if i not in marked:
            primes.append(i)
            marked.extend([i*j for j in range(2, limit)])
    return primes
