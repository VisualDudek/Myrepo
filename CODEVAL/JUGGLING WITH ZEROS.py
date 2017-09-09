
test = '00 0 0 00 00 0'
test = '00 0 0 000 00 0000000 0 000'

L = test.rstrip().split(' ')

LL = [ (x,y) for x,y in zip(L[::2],L[1::2])] # MEga sprytne jestem z siebie dumny

res = []
for x,y in LL:
    if x == '00':
        res += '1'*len(y)
    else:
        res += '0' * len(y)


print(LL)
print(''.join(res))
print(int(''.join(res), 2))
