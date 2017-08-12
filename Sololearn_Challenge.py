arr = [[]]*3
print(arr)
arr[0].append(7) #Nie rozumiem jak to zadziałało
try:
    print(arr[1][0])
except IndexError:
    print('0')
print(arr)

print('--------------------') # ------------------------

a=[]
for i in range(1,10):
    if (i%4==0) and (i%2==0):
        a.append(i)
print(a[0]+a[1])
print(a)

print('--------------------') # ------------------------

def foo(fn):
    def wrap():
        return '>{}'.format(fn())
    return wrap
@foo
def something():
    return 'result'


print(something())

print('--------------------') # ------------------------

y = [x if x ==1 else x*2 for x in ['1','2']][0]
print(y)

print('--------------------') # ------------------------

def func(num: int) -> int: #Nie rozumiem jak to działą
    return num

print(func(5))

print('--------------------') # ------------------------

*x, y = [1,2],[3,4],[5,6], #Dlaczego argumenty zostały przekazane do Listy a nie Tupli?
print(x,' ',y)
print(zip(*x + [y]))  # dlaczego taki dziwny output?
print(list(zip(*x + [y])))
print(list(zip(*x + [y]))[1][1]) #Dlaczego arr y jest ubrany w liste?

print('--------------------') # ------------------------

list1 = {'blue','green'}
list2 = {'green','blue'}
list1.add('black')
print(list((lambda x,y: x-y) (list1,list2)))
print((lambda x,y: x-y) (list1,list2)) # Nie wiedziałem że można w ten sposób przekazywać arg do lambdy

print('--------------------') # ------------------------

a = 6
roots = [x for x in range(1,a) if a%x==0] # Wypisuje dzialniki liczby a !!!
print(roots)

print('--------------------') # ------------------------

spam = {i:i%3+i for i in range (1,11)}
print(spam)
print(spam[spam[spam[2]]])

print('--------------------') # ------------------------

word1 = 'welcome'
word2 = 'home'
r = []
for x in word1:
    if x in word2:
        r.append(x)
print(r)
print(r[2]+r[1]+r[2])

print('--------------------') # ------------------------

print('{}{}'.format(*['h','i'])) # Nie rozumiem gwiazdki przed lista
# try:
#     print(''.join(*['h', 'i']))
# except:                             # Jak wykonywać kod dalej bez poprzestania na wyjątku?
#     print('Error: print(\'\'.join(*[\'h\', \'i\']))')

# print('{}{}'.format(['h','i']))     #Bardzo dziwnie opisuje ten błąd na Consoli
print(''.join(['h', 'i']))

print('--------------------') # ------------------------

strList = ['1','2','3','4','a']
intList = []
for i in strList:
    try:
        intList.append(int(i))
    except ValueError:
        intList = ['Something Not Int']
    finally:
        intList = []
print(str(len(intList)))

print('--------------------') # ------------------------
