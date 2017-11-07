
print(1.1 + 2.2)
1.1 + 2.2 == 3.3

sum([.1] * 10)
sum([.1] * 10) < 1.0

from math import fsum
fsum([.1] * 10)

38 / 5
38 // 5


from collections import defaultdict

d = {'raymond' : 'red'}
e = defaultdict(lambda : 'black')
e['rymond'] = 'green'

# difference is when key is missing
d['rachel']
e['rachel']

# --- Grouping with defaultdict

set()
list()
dict()

# Defaultdict creates a new container to store elements with a common feature
d = defaultdict(set)
d['t'].add('tom')
d['m'].add('mary')
d['t'].add('tim')
d['t'].add('tom')
d['m'].add('martin')

from pprint import pprint
pprint(d, width=40)

d = defaultdict(list)
d['t'].append('tom')
d['t'].append('tom')
pprint(d, width=40)

names = ''' david betty susan mary darlene sandy davin
            shelly becky beatrice tom micheal wallace'''.split()

d = defaultdict(list)
for name in names:
    feature = name[0] # name[-1]; len(name)
    d[feature].append(name)

# --- Key functions

# SELECT name FROM names ORDER BY len(name);
# How to say it in Python?
pprint(sorted(names, key=len))

# - Transposing with zip() and star-args
from itertools import zip_longest

list(zip('qwerty' ,'asdfghlm'))
list(zip_longest('qwerty' ,'asdfghlm'))
list(zip_longest('qwerty' ,'asdfghlm', fillvalue='X'))

# 3 rows by 2 colums
m = [
    [10, 20],
    [30, 40],
    [50, 60],
]
# Technics to manipulate structure m

list(zip([10, 20], [30, 40], [50,60]))
list(zip(*m))  # star unpack arg

# Flattening data with list comprehensions
pprint(m, width=20)

for row in m:
    for col in row:
        print(col)

#  ^== można użyć jako:
[x for row in m for x in row]


it = iter('abcd')
it
list(it)
