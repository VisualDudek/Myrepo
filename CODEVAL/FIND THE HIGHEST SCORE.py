

test = '72 64 150 | 100 18 33 | 13 250 -6'

L = test.split('|')
LL = [i.split() for i in L]
LLL = list(zip(*LL))

print(LLL)

res = ''
for i in LLL:
    L = []
    for j in range(len(i)):
        L.append(int(i[j]))
    res = res + ' ' + str(max(L))

print(res.lstrip())

#Uproszczenie

print(' '.join([str(max(map(int,x))) for x in LLL]))



test = '72 64 150 | 100 18 33 | 13 250 -6'

L = test.split('|')
LL = [map(int,i.split()) for i in L]
LLL = list(zip(*LL))

print(LLL)
print(' '.join([str(max(map(int,x))) for x in LLL]))