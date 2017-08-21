arr = [[]] * 3
print(arr)
arr[0].append(7)  # Nie rozumiem jak to zadziałało
try:
    print(arr[1][0])
except IndexError:
    print('0')
print(arr)

print('--------------------')  # ------------------------

a = []
for i in range(1, 10):
    if (i % 4 == 0) and (i % 2 == 0):
        a.append(i)
print(a[0] + a[1])
print(a)

print('--------------------')  # ------------------------


def foo(fn):
    def wrap():
        return '>{}'.format(fn())

    return wrap


@foo
def something():
    return 'result'


print(something())

print('--------------------')  # ------------------------

y = [x if x == 1 else x * 2 for x in ['1', '2']][0]
print(y)

print('--------------------')  # ------------------------


def func(num: int) -> int:  # Nie rozumiem jak to działą
    return num


print(func(5))

print('--------------------')  # ------------------------

*x, y = [1, 2], [3, 4], [5, 6],  # Dlaczego argumenty zostały przekazane do Listy a nie Tupli?
print(x, ' ', y)
print(zip(*x + [y]))  # dlaczego taki dziwny output?
print(list(zip(*x + [y])))
print(list(zip(*x + [y]))[1][1])  # Dlaczego arr y jest ubrany w liste?

print('--------------------')  # ------------------------

list1 = {'blue', 'green'}
list2 = {'green', 'blue'}
list1.add('black')
print(list((lambda x, y: x - y)(list1, list2)))
print((lambda x, y: x - y)(list1, list2))  # Nie wiedziałem że można w ten sposób przekazywać arg do lambdy

print('--------------------')  # ------------------------

a = 6
roots = [x for x in range(1, a) if a % x == 0]  # Wypisuje dzialniki liczby a !!!
print(roots)

print('--------------------')  # ------------------------

spam = {i: i % 3 + i for i in range(1, 11)}
print(spam)
print(spam[spam[spam[2]]])

print('--------------------')  # ------------------------

word1 = 'welcome'
word2 = 'home'
r = []
for x in word1:
    if x in word2:
        r.append(x)
print(r)
print(r[2] + r[1] + r[2])

print('--------------------')  # ------------------------

print('{}{}'.format(*['h', 'i']))  # Nie rozumiem gwiazdki przed lista
# try:
#     print(''.join(*['h', 'i']))
# except:                             # Jak wykonywać kod dalej bez poprzestania na wyjątku?
#     print('Error: print(\'\'.join(*[\'h\', \'i\']))')

# print('{}{}'.format(['h','i']))     #Bardzo dziwnie opisuje ten błąd na Consoli
print(''.join(['h', 'i']))

print('--------------------')  # ------------------------

strList = ['1', '2', '3', '4', 'a']
intList = []
for i in strList:
    try:
        intList.append(int(i))
    except ValueError:
        intList = ['Something Not Int']
    finally:
        intList = []
print(str(len(intList)))

print('--------------------')  # ------------------------


def decor(a, b):
    def sq(func):
        return func(a, b) * func(a, b)

    return sq


def subs(a, b):
    return (a - b)


def add(a, b):
    return (a + b)


f = decor(2, 3)
print(f(add) + f(subs))

print('--------------------')  # ------------------------

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.add(7)
set2.add(10)

print(set1 ^ set2)

print('--------------------')  # ------------------------                      DO KONSULTACJI strong private


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()

try:
    print(s.__egg)
except AttributeError:
    print('AttributeError -> __egg jest Strong Private wiec nie da sie do niego dostać z zewnatrz klasy')

print('--------------------')  # ------------------------

s = ['red', 'green', 'blue', 'white']
p = [1, 2, 3, 4]
r = ''

for i in range(len(s)):
    r += s[i][p[i]]
print(r)

print('--------------------')  # ------------------------

y = [x if x == 1 else x * 2 for x in ['1', '2']][0]
print(y)

print('--------------------')  # ------------------------                ZWRÓC UWAGE NA DWIE SKLADNIE LAMBDY

a = (lambda x: x ** 2 + 5 * x + 4)(-4)
print(a)

print('Autor')  # AUTORSKI POMYSL
a = (lambda x: x ** 2 + 5 * x + 4)
print(a(-4))

print('--------------------')  # ------------------------

x = {1: 2, 2: 3, 3: 4, 4: 6}
print(x.get(2, 0) % x.get(5, 4))

print('--------------------')  # ------------------------


def usingAny(num_list):
    if any([i < 10 for i in num_list]):
        print('True')
    else:
        print('False')


num_list = [42, 78, 22, 65, 14, 6]
usingAny(num_list)

print('Autor')  # AUTORSKI POMYSL + POROWNANIE DO FILTER
print(any([i < 10 for i in num_list]))
# róznica pomiedzy List Comprehention a filter()
print(list(filter(lambda x: x < 10, num_list)))
# filter() == generator expression
print(list(x for x in num_list if x < 10))

print(
    '--------------------')  # ------------------------  # UWAGA na nazywanie zmiennych tak jak wbudowane funkcje np. list

num = 1
L = []

while num < 5:
    L = L + [num]
    num += 1

print(len(L))

print('--------------------')  # ------------------------

a = lambda x: x != 1
b = [n for n in range(5)]

print(list(filter(a, b)))

print('--------------------')  # ------------------------

a = [0]


def pick_last(deck=a):
    val = deck[-1]
    deck.append(val + 1)
    return val


pick_last()
print(pick_last())

print('--------------------')  # ------------------------    UWAGA ++ oraz -- tlumaczy sie na +(+()) czyli nic


def p(a, b):
    t1 = ++a
    t2 = --b
    return (t1 * t2)


print(p(3, 2))

print('--------------------')  # ------------------------   UWAGA zapomniałem o zerze


def func1(a):
    x = []
    for i in range(a):
        if (i % 2 == 0):
            x.append('+' * i)
    return x

print(len(func1(6)))

print('--------------------')  # ------------------------

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[1:1:-1])

print('--------------------')  # ------------------------

func = lambda x: x%3 == 0
I = filter(func, range(10))
I = list(I)
print(len(I) + sum(I) + max(I))

print('--------------------')  # ------------------------     KONSULTACJE czy mozna uzywac dekoratora do def ?

def tripler(orig_func):
    def my_function(orig_val):
        return orig_func(orig_val)*3
    return my_function

@tripler
def doubler(user_input):
    return user_input*2

print(doubler(5))

print('--------------------')  # ------------------------

x = ('.'.join(str(i) for i in range(7,9)))[:2]
print(x)