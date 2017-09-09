
test = 'thisTHIS'
# test = 'AAbbCCDDEE'
# test = 'N'
# test = 'UkJ'

res = sum(int(x.islower()) for x in test.rstrip() )  #POPRAWIONE
res1 = len(list(filter(lambda x: x.islower(), test.rstrip())))
print(res1)
d = len(test.rstrip())

print('lowercase: {:.2f} uppercase: {:.2f}'.format(res*100/d,(d-res)*100/d))

