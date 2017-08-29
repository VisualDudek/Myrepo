
test = '9 0 6 | 15 14 9'

test = test.rstrip().split('|')

L = (str(int(x)*int(y)) for x,y in zip(test[0].split(),test[1].split()))

print(' '.join(L))