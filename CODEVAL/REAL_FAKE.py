'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        S = ''.join(test.split())
        sum = 0
        for x in range(0,len(S),2):
            sum += int(S[x])*2
        for x in range(1,len(S),2):
            sum += int(S[x])
        if sum%10 == 0:
            print('Real')
        else:
            print('Fake')
'''

# INPUT
#
# 9999 9999 9999 9999
# 9999 9999 9999 9993

test = '1234 5678 9876 5432'
S = ''.join(test.split())
sum = 0
for x in range(0,len(S),2):
    sum += int(S[x])*2
for x in range(1,len(S),2):
    sum += int(S[x])
print(sum%10)