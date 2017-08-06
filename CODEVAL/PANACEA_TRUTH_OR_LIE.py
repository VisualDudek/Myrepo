'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = test.split()
        virus = 0
        antivirus = 0
        B = True
        for x in L:
            if x == '|':
                B = False
            elif B:
                virus += int(x,16)
            elif not B:
                antivirus += int(x,2)
        if antivirus >= virus:
            print(True)
        else:
            print(False)
'''

# INPUT
# 64 6e 78 | 100101100 11110
# 5e 7d 59 | 1101100 10010101 1100111
# 93 75 | 1000111 1011010 1100010

test = '93 75 | 1000111 1011010 1100010'
L = test.split()
print(L)
print(int(L[0],16))
virus = 0
antivirus = 0
B = True
for x in L:
    if x == '|':
        B = False
    elif B:
        virus += int(x,16)
    elif not B:
        antivirus += int(x,2)
print(virus,' ',antivirus)
