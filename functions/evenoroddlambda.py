import itertools
l = lambda x: 'YES' if x % 2 == 0 else 'NO'
print(l(10))
# print(list(itertools.accumulate(l, range(0, 20, 3))))
print([i for i in range(0, 20, 3)])
print([l(i) for i in range(0, 20, 3)])