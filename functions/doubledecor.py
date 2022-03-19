def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner


# decorator function. it is similar to
# x = decorfun (num)
@decorfun
def num():
    return 5


print(num())


# with parameters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


# smart_divide(divide(8, 5))
@smart_divide
def divide(a, b):
    print(a/b)


divide(8, 0)

# for more
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


# similar to: out_func = star(percent(printer))
@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
