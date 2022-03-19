lst = [20, 30, 40, 234]
print(type(lst))
b = bytes(lst)
print(type(b))

#b[3]=22
byte_fncn = ['capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find',
             'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit',
             'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
             'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
             'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
             'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(len(byte_fncn))


num = b'you are \t Awesome.\nJust Awesome.'
print(type(num))
print(num.capitalize())
print(num.center(10))
print(num.count(b'are'))

# index: it returns initial index of matched substring of a string.
# it raise exception when substring is not found. it can't use
# conditional statement. It is applicable for list, strings and tuples.

# find: it returns initial index of matched substring of a string,
# but it returns -1 if not found. It can use conditional statement.
# It is only applicable for string.

# rfind for right -> left traverse
print(num.find(b'are'))
print(num.index(b'are'))
print(num.decode('utf-8'))
print(num.endswith(b'e'))
print(num.startswith(b'a'))
print(num.expandtabs(8))
print(bytes.fromhex('01 02 aa'))
print(num.hex())
print(num.isalnum())
print(num.isalpha())
print(num.isupper())
print(num.upper())
print(num.islower())
print(num.lower())
print(num.isascii())
print(num.isdigit())
print(num.isspace())
print(num.istitle())
print(num.title())

#
print(num.replace(b'\t', b''))

# rsplit for right -> left
print(num.split())

# lsplit: left -> right, rsplit: right -> left
print("split: ", num.split())
print("splitlines: ", num.splitlines())

# partition
print("partition: ", num.partition(b"Awesome"))
print("rpartition: ", num.rpartition(b"Awesome"))

# rjust, ljust
print("ljust: ", num.ljust(40, b'-'))
print("rjust", num.rjust(40, b'-'))

# zero fill
print('zero-fill: ', num.zfill(40))
#
print('join: ', b' '.join(num.split()))

# translate
print("transalate: ", num.translate(num.maketrans(b'A', b'a')))

# swapcase
print("swap-case: ", num.swapcase())


#bytes array
b1 = bytearray(lst)
print(type(b1))
b1[2] = 33
# print(dir(b1))
byte_arr_fncn = ['append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode',
                'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index',
                'insert', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace',
                'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
                'partition', 'pop', 'remove', 'replace', 'reverse', 'rfind', 'rindex',
                'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
                'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(len(byte_arr_fncn))
print(b1)
print([item for item in b1])
# print()
# print(bytearray.fromhex('A1 FF 92'))
print(b1.copy())
b1.remove(33)
print(b1)
b1.reverse()
print(list(b1))
print(b1.clear())
