x = 123


def display():
    x =678
    print(x)
    # use globals variables
    print(globals()['x'])


print(x)
z = display
z()
z()
z()
