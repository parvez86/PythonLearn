r=range(1,30,3)

range_fnct = ['count', 'index', 'start', 'step', 'stop']


for i in r:
    print(i)
print(dir(r))
print(r.index(7))
print(r.count(4))
print(r.start)
print(r.stop)
print(r.step)