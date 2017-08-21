
test = '7,8,9;8,9,10,11,12'
L = []

test = test.split(';')
L1 = list(int(x) for x in test[0].split(','))
L2 = list(int(x) for x in test[1].split(','))

for x in L1:
    if x in L2:
        L.append(x)                               # UWAGA mozna prosciej

L = [x for x in L1 if x in L2]                   # Uproszczenie for z if
                                                # LUB
L = list(set(L1) & set(L2))                      # uzywajac zbiorow

L = sorted(L)
L = list(str(x) for x in L)

# print(L1)
# print(L2)

if len(L) == 0:
    print('')
else:
    print(','.join(L))

print('---------------------------') # Skomplikujemy troche zadanie
# find intersection for nested lists

c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]

# OUTPUT: c3 = [[13,32],[7,13,28],[1,6]]

c3 = [list(filter(lambda x: x in c1, sublist)) for sublist in c2]
print(c3)
#LUB
c3 = [[x for x in sublist if x in c1] for sublist in c2]
print(c3)