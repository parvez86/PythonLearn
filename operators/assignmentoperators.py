a = b = c = 10
print(a, b, c)

x, y = 10, 5

x += y
print(x)

x *= y
print(x)

p = int(x)
q = float(x)
r = oct(x)
s = hex(x)
xc = x + 2j
print(xc)
print(type(xc))

# print(dir(p))
# print(dir(q))
# print(dir(r))
# print(dir(s))
# print(dir(xc))
int_fnctns = ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
float_fnctns =['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
complex_fnctns = ['conjugate', 'imag', 'real']

# oct & hex functions are likely string function
print('\n\nPractising int(%i) functions : ' % p)
print('bit length:', p.bit_length())
print('conjugate:', p.conjugate())
print('numerator:', p.numerator)
print('denominator:', p.denominator)
print('from bytes(little):', int.from_bytes(b'This function is too much irritating.', byteorder='little'))
print('from bytes(big):', int.from_bytes(b'This function is too much irritating.', byteorder='big'))

print('to byte(little):', p.to_bytes(10, byteorder='little'))
print('to bytes(big):', p.to_bytes(10, byteorder='big'))


print('imaginary part:', p.imag)   # return imaginary value
print('real part:', p.real)


print('\n\nPractising float(%.1f) functions: ' % q)
print('integer ratio:', q.as_integer_ratio())
print('is integer: ', q.is_integer())
print('conjugate:', q.conjugate())
print('hex:', q.hex())
print('fromhex:', float.fromhex(q.hex()))
print('imaginary part:', q.imag)
print('real part:', q.real)

print('\n\nPractising complex(%a) functions : ' % xc)
print('real part:', xc.real)
print('imaginary part: ', xc.imag)
print('conjugate: ', xc.conjugate())
