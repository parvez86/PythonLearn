import random
# print(dir(random))
random_func = ['betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate',
               'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
               'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
print('randint: ',random.randint(1,10))
print('random: ',random.random())
print('choice: ', random.choice([1,2,3,4,5,6,9,8,7]))
print('choices: ', random.choices([1,2,3,4,5,6,9,8,7],k=3))
print('gauss:', random.gauss(1.3, 15))
print('normalvariate: ', random.normalvariate(1.3,15))  #return a random floating point number with normal distribution.
print('randrange:', random.randrange(0, 15, 3))
# random.seed(3)
print('seed:',random.randint(1,10))
print('sample: ', random.sample([1,2,3,4,5,6,9,8,7],k=3))
print('uniform: ', random.uniform(10,15))   # for floating point
a = [1,2,3,4,5,6,9,8,7]
random.shuffle(a)
print('shufle: ', a)
print('triangular: ', random.triangular(3, 10, 9))