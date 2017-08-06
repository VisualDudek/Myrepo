'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a,b,c = [int(x) for x in list(test.rsplit())]
        L =[]
        for x in range(1,c+1):
            if x%a == 0 and x%b == 0:
                L.append('FB')
            elif x%a == 0:
                L.append('F')
            elif x%b == 0:
                L.append('B')
            else:
                L.append(str(x))
        print(' '.join(L))
'''

# INPUT SAMPLE:
# 3 5 10
# 2 7 15

test = input('INPUT --> ')
a,b,c = [int(x) for x in list(test.rsplit())]
L =[]
for x in range(1,c+1):
    if x%a == 0 and x%b == 0:
        L.append('FB')
    elif x%a == 0:
        L.append('F')
    elif x%b == 0:
        L.append('B')
    else:
        L.append(str(x))
print(' '.join(L))