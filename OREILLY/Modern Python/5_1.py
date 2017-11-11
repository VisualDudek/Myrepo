from collections import defaultdict
from pprint import pprint

"""
* defaultdict for accumulating data (tabulating)
* defaultdict for reversing a one-to-many mapping 
                              one-to-one

"""

d = defaultdict(list)
d['raymond'].append('red')
d['rachel'].append('blue')
d['matthew'].append('yellow')

pprint(d)

d['raymond'].append('mac')
d['rachel'].append('pc')
d['matthew'].append('vtech')

pprint(d)
pprint(dict(d))

# Deafaultdict: groupping, accumulation

# Model one-to-many: dict(one, list_of_many)

e2s = {
    'one' : ['uno'],
    'two' : ['dos'],
    'three' : ['tres'],
    'trio' : ['tres'],
    'free' : ['libre', 'gratis'],
}

pprint(e2s)

# Q: How do you reverse a one-to-many mapping?
s2e = defaultdict(list)
for eng, spanwords in e2s.items():
    for span in spanwords:
        s2e[span].append(eng)


pprint(s2e)

# What id dict is one-to-one?
e2s = dict(one='uno', two='dos', three='tres')
#  use dict comprehension
s2e = {span: eng for eng, span in e2s.items()}