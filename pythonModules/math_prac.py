import math
# print(dir(math))
func_list = ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
print('Math Function #: ', len(func_list))
print('Functions: ', func_list)

print('Exploring some functions: ...................')
print('degrees: ', math.pi/2)
print('exp: ', math.exp(2))         # math.e**2
print('eucleadian distance(dist): ', math.dist((2,3,1),(1,1,1)))
print('exp(e): ', math.e)
print('erf: ', math.erf(2.3))
print('fabs: ', math.fabs(-2.3))    # fmod, fsum, frexp,
print('Factorial: ', math.factorial(5))
print('multiply: ', math.prod([1,2,3,4,5]))
print('sqrt: ', math.sqrt(8))   # isqrt() -> return integer part
print('gcd: ', math.gcd(3,5))
print('remainder: ', math.remainder(7, 5))
print('hypotenuse: ', math.hypot(3,4))
print('log1p', math.log1p(3))       #log(1+3)
print('modf:', math.modf(3.5))     # return (fractinal, integer)
print('isclose:', math.isclose(2.31111111, 2.31111112))
print('permutation: ', math.perm(4,3))
print('combination: ', math.comb(4,3))
print('truncate: ', math.trunc(2191.819))   # only integer part