def largest_palindrome(max_factor, min_factor):
    max_p = set()
    pals = palindromes(max_factor, min_factor)
    maxv = max([p[0]*p[1] for p in pals])
    for p in pals:
        if p[0]*p[1] == maxv:
            max_p.add(p)
    return maxv, max_p


def smallest_palindrome(max_factor, min_factor):
    min_p = set()
    pals = palindromes(max_factor, min_factor)
    minv = min([p[0]*p[1] for p in pals])
    for p in pals:
        if p[0]*p[1] == minv:
            min_p.add(p)
    return minv, min_p


def palindromes(max_factor, min_factor):
    lista = []
    l1 = [(i, j)
        for i in range(min_factor, max_factor+1)
        for j in range(i, max_factor+1)]
    for l in l1:
        if l not in lista:
            lista.append(l)
    palindromes = []
    for x in lista:
        product = x[0]*x[1]
        if product < 10:
            palindromes.append(x)
        elif str(product) == str(product)[::-1]:
            palindromes.append(x)
    # ~ print(palindromes)
    return palindromes

# ~ value, factors = smallest_palindrome(min_factor=1, max_factor=9)
# ~ self.assertEqual(value, 1)
# ~ self.assertFactorsEqual(factors, {(1, 1)})
# ~ print(value)
# ~ print(factors)

# ~ print(type({(1, 9), (3, 3)}))

# ~ t1 = (1, 2)
# ~ t2 = (3, 4)
# ~ s1 = set()
# ~ s1.add(t1)
# ~ s1.add(t2)
# ~ print(s1)

# ~ value, factors = largest_palindrome(min_factor=1, max_factor=9)
# ~ print(value)
# ~ print(factors)

# ~ pals = palindromes(min_factor=1, max_factor=9)
# ~ print(max([p[0]*p[1] for p in pals]))
# ~ print(min([p[0]*p[1] for p in pals]))
