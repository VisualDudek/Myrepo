app = 'Enki'
streak = 3

print('This is Phyton workout number %d with %s' % (streak, app))

# The is operator
# will evaluate to true if the vars on either side of the operator point to the same object !!!

str = 'Marcin'
isstr = str
print(str is isstr)

L1 = [1,2,3]
L2 = [1,2,3]
print(L1 is L2) #Will print False! The is operator is used to match INSTANCES instead of vars