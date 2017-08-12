'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = test.split()
        a,b = int(L[0]),int(L[1])
        z = 0
        for x in range(1,b+1):
            #print('{0:b}'.format(x)) #Czy jest inny sposób na zamiane bazy
            s = '{0:b}'.format(x)
            if s.count('0') == a:
                z += 1
        print(z)
'''


# INPUT
# 1 8
# 2 4

test = '1 8'
L = test.split()
a,b = int(L[0]),int(L[1])
z = 0
for x in range(1,b+1):
    print('{0:b}'.format(x)) #Czy jest inny sposób na zamiane bazy
    s = '{0:b}'.format(x)
    if s.count('0') == a:
        z += 1
print(z)