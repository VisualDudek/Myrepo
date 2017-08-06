'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = test.split()
        n = int(L[-1])
        L = L[0:len(L)-2]
        for x in range(n):
            i = 0
            while int(L[i]) <= int(L[i+1]):
                i += 1
            L[i],L[i+1] = L[i+1],L[i]
        print(' '.join(L))
'''

# INPUT
#
# 4 3 2 1 | 1
# 5 4 3 2 1 | 2
# 11 21 32 35 41 1 53 9 72 | 8

test = '11 21 32 35 41 1 53 9 72 | 8'
L = test.split()
n = int(L[-1])
L = L[0:len(L)-2]
for x in range(n):
    i = 0
    while int(L[i]) <= int(L[i+1]):
        i += 1
    L[i],L[i+1] = L[i+1],L[i]
    print(L)
print(' '.join(L))