tpl=(40,50,40,"XYZ")
print(dir(tpl))
tuple_fnct = ['count', 'index']



print(tpl)
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("XYZ"))

lst = [67,34,"XYZ"]
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))   # convert tuple to list
print(tpl1)
print(list(tpl))
