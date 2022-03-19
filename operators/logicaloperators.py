x = 20
y = 30
print("X: ", x, "Y: ", y)
print((x == 25 and y == 30))

print((x == 25 or y == 31))

print(not(x == 25 or y == 31))


print('binary x: ', bin(x))
print('binary y: ', bin(y))
print('bitwise not x: ', ~int(x))
print('bitwise not y: ', ~int(y))
print('bitwise and: ', x & y)
print('bitwise or:', x | y)
print('bitwise xor: ', x ^ y)
print('bitwise left shift: ', x << 3)    # multiply by 3**2
print('bitwise right shift:', x >> 2)    # divide by 2**2
