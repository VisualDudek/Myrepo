'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L=[]
        for x in test:
            if x.isalpha():
                L.append(x.lower())
            else:
                L.append(' ')
        T = ''.join(L)
        T = T.split()
        T = ' '.join(T)
        print(T)
'''


# INPUT SAMPLE:
#(--9Hello----World...--)
#Can 0$9 ---you~
#13What213are;11you-123+138doing7

test = '(--9Hello----World...--)'
L=[]
for x in test:
    if x.isalpha():
        L.append(x.lower())
    else:
        L.append(' ')
T = ''.join(L)
print(T)
T = T.split()
print(T)
T = ' '.join(T)
print(T)

print('----------------------') # BRAIN
# Syntetyczny IF

L = list([' ',x.lower()][x.isalpha()] for x in test)
print(L)
print(''.join(L))
print(''.join(L).split())
print(' '.join(''.join(L).split()))

