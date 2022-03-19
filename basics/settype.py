# s = {10, 20, 30, "XYZ", 10, 20, 10}
s = set([10, 20,30, "XYZ", 10, 20, 10])
s1 = s.copy()
s1.add(70)
s3 = {10, 30}

set_fnctns = [ 'add', 'clear', 'copy', 'difference', 'difference_update',
               'discard', 'intersection', 'intersection_update',
               'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
               'symmetric_difference', 'symmetric_difference_update',
               'union', 'update']
print(len(set_fnctns))
print(set_fnctns)

s.update([88, 99])

print(type(s))
print(type(s1))
print(type(s3))
print('S(After update): ', s)
print('S1: ', s1)
print('S3: ', s3)


#print(s*3)
s.remove(30)
print('S (after remove 30): ', s)
print('After using union(s, s1): ', s.union(s1))
print('After using intersection(s, s1): ', s.intersection(s1))
print('After using difference(s1, s): ', s1.difference(s))
print('Is disjoint (s,s1): ', s.isdisjoint(s1))
print('Is subset(s3,s1):', s3.issubset(s1))
print('Is superset(s1, s3): ', s1.issuperset(s3))
print('Symmetric difference (s,s1): ', s.symmetric_difference(s1))       # return uncommon word (both set)
s.symmetric_difference_update(s1)
print('After using symmetric_difference update(s,s1): ', s)
s3.intersection_update(s)   # remove umcommon item
print('After using intersection_update(s3, s1): ', s3)
s.difference_update(s1)     # remove common item
print('After using difference_update(s,s1): ', s)
s.add(50)
print('After adding (s, 50): ', s)
s.discard(88)
print('After discarding(s, 88): ', s)
s.update(s1)
print('After updating(s, 20): ', s)

# frozen set -> create immutable set
# print(dir(f))
# frozen_set_fncts = ['copy', 'difference', 'intersection', 'isdisjoint', 'issubset',
# 'issuperset', 'symmetric_difference', 'union']
f = frozenset(s)
print('Frozen set (s) f: ', f)
print('is disjoint (f, s1): ', f.isdisjoint(s1))
# f.remove(20)  # frozen set can't be modified
