from collections import Counter
# colections -> counter, deque, recipes, namedtuple, OrderedDict, defaultdict
lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print("Counter:",Counter(lst))
print("Counter:",Counter("aabsbsbsbhshhbbsbs"))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))
# Methods with Counter()
c = Counter(words)

print(c.most_common(2))
# print(dir(Counter()))

collections_func_list = ['clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values']
print('Function #: ', len(collections_func_list))
print('Functions: ', collections_func_list)

print('Python Collections Counter functions: ')
d= c.copy()
print("Copied: ", d)
print('Elements: ', d.elements())
print('items: ', d.items())
print('keys: ', list(d.keys()))
print('values: ', d.values())
print('Most common: ', d.most_common(3))
print('get: ', d.get('many'))
# print('fromkyes: ', d.fromkeys([c.keys()]))
print('pop: ', d.pop('many'))
print('popitems: ', d.popitem())
print('update: ', d.update())
print('subtract: ', d.subtract(c.popitem()))
print('setdefaults: ', d.setdefault(int))
print('Clear: ', d.clear())
d = c.copy()
d.popitem()
d.popitem()
print('addition: ', c+d)
print('subtraction: ', c-d)
print('intersection: ', c&d)
print('union: ', c|d)
