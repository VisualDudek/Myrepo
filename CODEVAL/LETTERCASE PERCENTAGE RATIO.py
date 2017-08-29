
test = 'thisTHIS'
test = 'AAbbCCDDEE'
test = 'N'
test = 'UkJ'

res = sum(1 for x in test.rstrip() if x.islower())
d = len(test.rstrip())

print('lowercase: {:.2f} uppercase: {:.2f}'.format(res*100/d,(d-res)*100/d))

