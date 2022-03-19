from functools import reduce
from itertools import accumulate
import math
lst = [1, 2,  4, 3, 5]
prod = 1

for i in lst:
    prod *= i
print("Product is: ", prod)

# 1 * 2 * 3 * 4 * 5 * 3

# it returns the summary
print("product: ", reduce(lambda x, y: x*y, lst, 3))

print("product: ", list(accumulate(lst, lambda x, y: x*y)))


# print max  -> max > 8 ?
print("Max: ", reduce(lambda a, b: a if a > b else b, lst, 8))


# filter: it returns the values that accept the conditions
print("Odds: ", list(filter(lambda x: x & 1 == 0, lst,)))
