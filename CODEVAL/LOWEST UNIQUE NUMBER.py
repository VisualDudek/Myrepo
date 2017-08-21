
test = '8 4 6 5 5 2 8 6 6 7 5 9 5 3 5 2 2 8 3 1'

X = [int(x) for x in test.split()]
L = sorted(X)
L = list(filter(lambda x: L.count(x) == 1 , L))

if len(L) == 0:
    print(0)
else:
    print(X.index(L[0])+1)

