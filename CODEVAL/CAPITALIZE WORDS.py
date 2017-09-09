
test = 'Hello world marcin'

L = test.split()

for x in range(len(L)):
    L[x] = L[x][0].upper() + L[x][1:]

print(' '.join(L))

# Uproszczenie

L = test.split()
print(L)

print(' '.join([ x[0].upper()+x[1:] for x in L]))

# Uproszczenie lepiej używać generator expresiona ponieważ zużywa mniej pamięci

print(' '.join(( x[0].upper()+x[1:] for x in L)))
