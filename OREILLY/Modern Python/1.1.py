
print ('Hello world')

# f-string
x = 10
print(f'Number {x:08d}')
print(f'Number {x ** 2 :08d}')

# Bardzo bobry przykład użycia f-string
x = 10
# raise ValueError(f'Expected {x!r} to a float no a {type(x).__name__}')

# Counter object
from collections import Counter
d = Counter()
print(d['dragon'])
d['dragon'] += 1
print(d['dragon'])
print(d)

c = Counter('red green red blue red blue green'.split())
c.most_common()
c.most_common(2)
list(c.elements())
list(c)
list(c.elements())
list(c)

# Sprawdzanie jakie metody posiada dany obiekt
dir(Counter)
list(filter(lambda x: not x.startswith('_'), dir(Counter)))

# Sort
s = [10, 5, 70, 2]
s.sort() #sort in place
# OR
t = sorted(s)

sorted('cat')

# Lambda expresions
    #  lambda -> make function
lambda x: x ** 2
(lambda x: x ** 2)(5)

f = lambda x,y: 3*x + y
f(3, 8)

x = 10
y = 20
f = lambda : x*y
f()

# Chained comparison
x = 15
x > 6 and x < 20
6 < x < 20

# Random ustawienie seed tak żeby można było powtarzać doświadczenia na tych samych losowych liczbach
from random import *
random()
seed(8675309)
random()

# Przykłady rozkładów
uniform(100,110)
triangular(100,110)
gauss(100,15)
expovariate(20)

from statistics import mean
data = [triangular(100,200) for i in range(1000)]
mean(data)

# Lib/random - Functions for seq
from random import choice, choices, sample, shuffle
outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
choice(outcomes)
choices(outcomes, k=10)  # Losowanie z powtorzeniami
Counter(choices(outcomes, k=10))
Counter(choices(outcomes, [5,4,3,2,1] ,k=10))

shuffle(outcomes)   # shuffle IN-PLACE tak taj sorted()
sample(outcomes,k=3)

sample(range(1, 57), k=6 ) # Przyklad losowania bez powtórzen
sorted(sample(range(1, 57), k=6 ))

#jedno jest szczególnym przypadkiem drugiego
sample(outcomes, k=1)[0]
choice(outcomes)

shuffle(outcomes)
sample(outcomes, k = len(outcomes))
