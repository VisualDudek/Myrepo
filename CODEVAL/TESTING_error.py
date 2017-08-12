'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = test.split()
        bugs = 0
        for i in range(int((len(L)-1)/2)):
            for x in range(len(L[i])):
                if L[i][x] != L[-1-i][x]:
                    bugs += 1
        #print(bugs)
        if bugs > 1 and bugs <= 2:
            print('Low')
        elif bugs > 2 and bugs <= 4:
            print('Medium')
        elif bugs > 4 and bugs <= 6:
            print('Low')
        elif bugs > 6 :
            print('Critical')
        else:
            print('Done')
'''


# INPUT
# Heelo Codevval | Hello Codeeval
# hELLO cODEEVAL | Hello Codeeval
# Hello Codeeval | Hello Codeeval

test = 'gTvqtzEKVSUcSuglDJkp | zJlTcVSDUqgEvKktgSup'
L = test.split()
print(L)
bugs = 0
for i in range(int((len(L)-1)/2)):
    for x in range(len(L[i])):
        if L[i][x] != L[-1-i][x]:
            bugs += 1
print(bugs)
if bugs > 1 and bugs <= 2:
    print('Low')
elif bugs > 2 and bugs <= 4:
    print('Medium')
elif bugs > 4 and bugs <= 6:
    print('Low')
elif bugs > 6 :
    print('Critical')
else:
    print('Done')
