import glob

glob.glob('*.py')

with open('congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())

it = iter('abcdefg')
next(it)
next(it)
list(it)


import csv
with open('congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)


# --- Tuple unpacking
t = ('Raymond', 'Hettinger' , 54, 'python@rcn.com')
type(t)
len(t)

fname, lname, age, email = t


# --- Loop idioms
names = 'raymond rachel matthew'.split()
colors = 'red blue yellow'.split()
cities = 'austin dallas austin houston chicago dallas austin'.split()

# old fashion way
for i in range(len(names)):
    print(names[i].upper())
    #       ^== wrong doing

# Faster shorter simpler
for name in names:
    print(name.upper())

# -- enumerate
# old fashion way
for i in range(len(names)):
    print(i+1, names[i])
#          ^== wrong doing

for i, name in enumerate(names, start=1):
    print(i, name)

# -- reversed
for i in range(len(colors) - 1, -1, -1 ):
    print(colors[i])

for color in reversed(colors):
    print(color)

# -- zip  paring two lists
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], colors[i])

# better way
for name, color in zip(names, colors):
    print(name, color)

# -- sorted()
for color in sorted(colors):
    print(color)

# using key-func
for color in sorted(colors, key=len):
    print(color)

# -- set  eliminating duplicates
for city in sorted(set(cities)):  #SQL: SELECT DISTINCT city FROM Cities ORDER BY city
    print(city)

# functional programing -> using one output as input
for i, city in enumerate(map(str.upper, sorted(set(cities)))):
    print(i, city)


# --- Incrementing instances of Counter
import collections
c = collections.Counter()
c['red'] += 1
print(c)
c['blue'] += 1
c['red'] += 1
print(c)
print(c.most_common())
print(list(c.elements()))


# --- Assertions
assert 5 + 3 == 8
assert 5 + 3 == 10

