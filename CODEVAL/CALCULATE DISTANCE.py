
test = '(47, 43) (-25, -11)'

# Czy da się prościej usunac znaki ( ) , za pomocą reg expresion?
L = test.replace('(','').replace(')','').replace(',','').split()
L = [int(x) for x in L]

res = (L[0] - L[2])**2 + (L[1] - L[3])**2

# Jak formatować fixed digits after decimal point? Czy jest latwiejszy sposob?
print('{0:.0f}'.format(res**.5))
