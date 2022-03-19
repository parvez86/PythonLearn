lst = [10,20,'Bharath',-10,30.5]
lst_fncts = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
             'pop', 'remove', 'reverse', 'sort']

lst_fncts2 = list()
lst_fncts2 =lst_fncts.copy()
print(lst_fncts2)
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))


# append adds a single element
# where as extends concatenate 2 lists (for inserting multiple element)
lst.append(40)
lst.remove('Bharath')
del(lst[1])
print(lst)

lst.extend([20, 'Sp', 40])
print(lst)
print(lst.index('Sp'))
lst.remove('Sp')
print(max(lst))
print(min(lst))
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst.pop()
print(lst)
lst.insert(3, 99)
print(lst)
lst.sort(reverse=True)
print(lst)

lst.clear()
print(lst)
# print(dir(lst))
print(len(lst_fncts))