from random import *
from statistics import *
from collections import *

# Main topic: resampling statistics
# YT: Statistics for Hackers by Jake Vanderpls

#*** Six roulette wheels spin -- 18 red 18 black 2 green
choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)

# Czytelniejsze rozwiązanie
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
choice(population)

[choice(population) for _ in range(6)]
Counter([choice(population) for _ in range(6)])

# Można inaczej
choices(population, k=6)
Counter(choices(population, k=6))

# Big idea!
Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
# ^----- This is a big idea with little code

deck = Counter(tens=16, low=36)
# How to get list of elements?
deck = list(deck.elements())

deal = sample(deck, k=20)
Counter(deal)

deal = sample(deck, k=52)
remainder = deal[20:]
Counter(remainder)

# Calość razem
deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, k=52)
remainder = deal[20:]
Counter(remainder)  #teraz mozna oszacowac szanse

#*** 5 or more heads from 7 spins of a biased coin
pop = ['heads', 'tails']
wgt = [6, 4]
cumwgt = [0.60, 1.00]

choices(pop, cum_weights=cumwgt, k=7)
# pamietaj o metodach list()
choices(pop, cum_weights=cumwgt, k=7).count('heads')

choices(pop, cum_weights=cumwgt, k=7).count('heads') >= 5

# Lambda w uzyciu
trial = lambda : choices(pop, cum_weights=cumwgt, k=7).count('heads') >= 5
trial()

# Przeprowadzenie eksperymentu
n = 10000
sum(trial() for _ in range(n)) / n

# Compare to the analytics approach
from math import factorial as fact
fact(4)

def comb(n, r):
    # return fact(n) / fact(r) / fact(n-r)
    return fact(n) // fact(r) // fact(n-r)

comb(10, 3)

ph = 0.6
# 5 heads out of 7 spins
ph ** 5 * (1 - ph) ** 2 * comb(7, 5)
# 6 heads out of 7 spins
ph ** 6 * (1 - ph) ** 1 * comb(7, 6)
#  7 heads out of 7 spins
ph ** 7 * (1 - ph) ** 0 * comb(7, 7)

# 0.2612736 + 0.0279935999 + 0.1306367999 = 0.4199039998
#                            theoretical result ==^
sum(trial() for _ in range(n)) / n
#  >>> 0.4174  <== empirical result

# --- Prob. that the median of 5 samples falls a middle quartile
from random import sample

sample(range(10000), 5)
median(sample(range(10000), 5))

n = 10000
sorted(sample(range(n), 5))[2]
trial = lambda : n //4 < sorted(sample(range(n), 5))[2] <= 3 * n // 4
sum(trial() for _ in range(n)) / n




