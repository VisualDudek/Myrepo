
test = '70.920 -38.797 14.354 99.323 90.374 7.581'

L = sorted([float(x) for x in test.split()])

# print(L)

L = ['{0:.3f}'.format(x) for x in L]


print(' '.join(L))


# Czy da sie zmniejszyc zapotrzebowanie na pamiec? i jak to sprawdzic?

