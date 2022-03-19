dict1 = {1: "john", 2: "bob", 3: "bill"}
dict_fnctns = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
               'popitem', 'setdefault', 'update', 'values']

print(dict1)
print(len(dict_fnctns))
print(dict_fnctns)
print(dict1.items())

# k=dict1.keys()
# for i in k:print(i)
print('Keys: ', dict1.keys())
print('Values: ', dict1.values())
print(dict1.get(2))

x = tuple(dict1.values())
print(x)
y = 2
dict2 = dict.fromkeys(x, y)
print(dict2)

print(dict2.popitem())
print(dict2)
dict2.update({'bob': '3'})
print(dict2)
print(dict2.setdefault('bob', 2))
print(dict2.setdefault('bill', 4))  # return the item value otherwise set default value.

# v=dict1.values()
# for i in v:print(i)

print(dict1[3])

del dict1[2]
print(dict1)

dict1.clear()
print(dict1)
# print(dir(dict1))