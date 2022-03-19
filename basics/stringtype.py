s = " you are Awesome "
fnctn = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
         'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
         'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
         'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
         'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
         'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
         'zfill']
print(s)
print(len(fnctn))

s1 = """You are
the creator
of your destiny"""
print(s1)

print(s[2])

print(s*3)

# range
print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])
print(len(s[-3:-1]))

print(s[0:9:2])
print(s[15::-1])    # reverse order
print(s[::-1])      # reverse order

print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.ljust(35) + 'check ljust')
print(divmod(56, 5))
print(id(s))
print(s.find("awe", 0, 8))
print(s.index('we'))
print(s.rindex('we'))
print(s.count("a"))
print(s.replace("Awesome", "super"))
print(s.translate(s.maketrans('A', 'a')))
print(s.partition('super'))
print(s.rpartition('super'))
print(iter(s))

print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.lstrip().capitalize())
print(s.center(40))

# it removes all case distinction (lower()). it is used for caseless comparison.
print(s.casefold())
t = s.casefold() + '\tt\th\ti\ts is for tabs.'
print(t)
print(s.encode())
print(s)
print(s.encode().decode())
print(s)
print(s.rstrip().endswith('e'))
t = t.expandtabs(2)
print(t)
r = '{name} is {age} years old. His height is {height: .2f} ft'
print(r.format(name='Sp', age=25, height=5.3))
profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]}

# Use of format_map() function
print('{name[0]} is an {profession[0]} and he is {age[0]} years old.'.format_map(profession))

print('{name[1]} is an {profession[1]} and he is {age[1]} years old.'.format_map(profession))
print(profession['name'][0].isidentifier())
print(('1sju3323').isidentifier())  # checks whether identifier is valid or not

