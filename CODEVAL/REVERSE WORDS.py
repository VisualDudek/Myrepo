'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = test.rsplit()
        print(' '.join(L[::-1]))
'''

# INPUT SAMPLE:
#Hello World
#Hello CodeEval

test = input('INPUT --> ')
L = test.rsplit()
print(' '.join(L[::-1]))