'''
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        L = []
        for x in list(test.rsplit()):
            x = list(x)
            (x[0],x[len(x)-1]) = (x[len(x)-1],x[0])
            x = ''.join(x)
            L.append(x)
        print(' '.join(L))
'''

# CHALLENGE DESCRIPTION:
#
# Write a program that, given a sentence where each word has a single digit positive integer as a prefix and suffix,
# swaps the numbers while retaining the word in between. Words in the sentence are delimited from each other by a space.
#
# INPUT SAMPLE:
#
# The first argument is a path to a file. Each line of the input file contains one test case represented by a sentence.
# Each word in the sentence begins and ends with a single digit positive integer i.e. 0 through 9.
# Assume all characters are ASCII.
#
# 4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
# 5Nobody5 7expects3 5the4 6Spanish4 9inquisition0
#
# OUTPUT SAMPLE:
#
# For each test case, print to standard output the sentence obtained by swapping the numbers surrounding each word,
# one per line.
#
# 0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5
# 5Nobody5 3expects7 4the5 4Spanish6 0inquisition9

test = input('INPUT --> ')
L = []
for x in list(test.rsplit()):
    x = list(x)
    (x[0],x[len(x)-1]) = (x[len(x)-1],x[0])
    x = ''.join(x)
    L.append(x)
print(' '.join(L))