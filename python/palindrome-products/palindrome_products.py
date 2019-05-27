def largest_palindrome(max_factor, min_factor):
    pass


def smallest_palindrome(max_factor, min_factor):
    pass

x1 = 1
x2 = 9
lista = []
l1 = [(i, j)
      for i in range(x1, x2+1)
      for j in range(i, x2+1)]
for l in l1:
    if l not in lista:
        lista.append(l)

palindromes = []
max = 0
for x in lista:
    product = x[0]*x[1]
    if product < 10:
        palindromes.append(x)
        if product > max:
            max = product
    elif str(product) == str(product)[::-1]:
        palindromes.append(x)
        if product > max:
            max = product


print(max)
