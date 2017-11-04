from random import *
from collections import *
from statistics import *
import matplotlib.pyplot as plt


# --- Bootstrapping to estimate the confidence interval on a sample of data
timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98,
           8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
mean(timings)
stdev(timings)
# Build a 90% confidence interval

def bootstrap(data):
    return choices(data, k=len(data))
# some date will be double and some left out
bootstrap(timings)

n = 10000
means = sorted(mean(bootstrap(timings)) for _ in range(n))
len(means)
means[:20]
means[-20:]

# n * .05 = 500
means[500]
print(f'The observed mean of {mean(timings)}')
print(f'Falls ia na 90% confidence interval from {means[500] :.1f} to {means[-500] :.1f}')

# --- Statistical significance of the difference of two means
#  \-> shuffle slicing mean
drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
print(f'Możemy zaobserwować rożnicę w średniej pomiędzy drug: {mean(drug) :.2f} vs placebo: {mean(placebo) :.2f}')
diff = mean(drug) - mean(placebo)

# If we reshuffle (permutting, relabeling) the participants,
# is the new mean diff the same or more extreme than be observed.
comb = drug + placebo
nd = len(drug)
shuffle(comb)
comb[:nd]
comb[nd:]

def trial():
    shuffle(comb)
    return mean(comb[:nd]) - mean(comb[nd:]) > diff

n = 10000
res = sum(trial() for _ in range(n)) / n
print(f'p-value = {res :.4f}')
#       ^== p-value likelihood that the outcome was solely due to chance

# Na koniec narysujemy coś
def trial_():
    shuffle(comb)
    return mean(comb[:nd]) - mean(comb[nd:])

n = 10000
data = list(trial_() for _ in range(n))

num_bins = 50
n, bins, patches = plt.hist(data, num_bins, )
# plt.tight_layou()
plt.show()

# --- Single server queue simulation
average_arrival_interval = 5.6
average_service_time = 5.0 # HINT change from 5.0 to 4.8 has a profond effect on Mean and Median
stdev_service_time = 0.5  # HINT does the consistency matter? => change stdev from 0.5 to 0 and check out

num_waiting = 0
arrivals = []
starts = []
arrival = service_end = 0.0
for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival += expovariate(1.0 / average_arrival_interval)
        arrivals.append(arrival)
    else:
        num_waiting -= 1
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)]
print(f'Mean wait: {mean(waits):.1f}. Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}. Max wait: {max(waits):.1f}.')

num_bins = 50
n, bins, patches = plt.hist(waits, num_bins, )
# plt.tight_layou()
plt.show()