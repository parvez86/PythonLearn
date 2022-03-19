def calc(a, b):
    x = a+b
    y = a-b
    z = a*b
    u = a/b
    return x, y, z, u


label = ["Summation", "Subtraction", "Multiplication: ", "Division"]
result = calc(10, 5)
print(result)
for key, val in zip(label, result):
    print(key, ": ", val)
