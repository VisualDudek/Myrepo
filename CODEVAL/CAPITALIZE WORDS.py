
test = 'Hello world'

L = test.split()

for x in range(len(L)):
    L[x] = L[x][0].upper() + L[x][1:]

print(' '.join(L))