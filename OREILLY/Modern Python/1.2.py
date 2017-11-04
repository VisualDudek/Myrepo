from random import *
random()
seed(7894) # step to reproduce research
random()

uniform(100,110)
triangular(100,110)
gauss(100,15) # parametry dla rozkladu IQ ???
expovariate(20)

from statistics import mean, stdev
data = [uniform(100,200) for _ in range(1000)]
mean(data)
stdev(data)