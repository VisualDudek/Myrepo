from collections import Counter

test = '8 4 6 5 5 2 8 6 6 7 5 9 5 3 5 2 2 8 3 1'

X = [int(x) for x in test.split()] # lepij map bo zwraca map obj.
L = sorted(X)
L = list(filter(lambda x: L.count(x) == 1 , L))

if len(L) == 0:
    print(0)
else:
    print(X.index(L[0])+1)


##########

l = map(int, test.split())
c = Counter(l)
# ll = [x for x, _ in filter(lambda item, n: n == 1, c.most_common())]
# ll =
# print(min(ll))

#######

print(min([x for x, n in Counter(map(int, test.split())).most_common() if n == 1]))

###################################################

l = map(int, test.split())

s1 = set()
s2 = set()

for i in l:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

print(min(s1-s2))

