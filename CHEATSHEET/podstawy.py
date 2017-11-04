
# Table of content
#  1 Operations
#  2 Lambda


# --- Operations
4 / 2  # => output is float
4 // 2  # => floor div. output is int.


# --- Lambda
#   ^== make function

lambda x: x ** 2
(lambda x: x ** 2)(5)

f = lambda x,y: 3*x + y
f(3, 8)

x, y = 10, 20
f = lambda : x*y  #no argument
f()

# Lambdas are usually used in conjunction with data processing functions such as
# filter, map and reduce
#          ^        ^== Summarizing !!! Lib/functools
#          ^== Transformation

list(filter(lambda x: x % 2 == 0 , range(0,11)))

list(map(lambda x: x * 2 , range(0,11)))

from functools import reduce
reduce(lambda x,y: x + y , range(0,11))

# Using no arg Lambdas for simulations
#  EX: empirycznie ile razy liczba losowa z przedzialu 0-1 jest wieksza od 0.5
#  TIP: True and False mozna sumowac
from random import random

trial = lambda : random() > 0.5
n = 100000
sum(trial() for _ in range(n)) / n