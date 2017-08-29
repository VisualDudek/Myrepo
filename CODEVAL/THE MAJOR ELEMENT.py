
test = '92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19'

L = [int(x) for x in test.rstrip().split(',')]
s = set(L)

d = {x:L.count(x) for x in s}
p = sorted(d, key=d.__getitem__, reverse=True)

print(d)

if d[p[0]] > len(L)/2:
    print(p[0])
else:
    print('None')
