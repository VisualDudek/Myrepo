print(__name__)

import random
import timeit
import matplotlib.pyplot as plt


N = 10

numbers = [random.randint(1,100) for _ in range(N)]

s = sum(numbers)
res = 1000
lewy = 0

for i in range(N):
    lewy += numbers[i]
    prawy = s - lewy
    res = min(abs(prawy-lewy),res)

print(numbers)
print(res)

def TCtime():
    code1 = '''
s = sum(numbers)
res = 1000
lewy = 0

for i in range(len(numbers)):
    lewy += numbers[i]
    prawy = s - lewy
    res = min(abs(prawy-lewy),res)
    '''

    setup = 'import random\nnumbers = '

    xlist, ylist = [], []

    print('N\tSum Time')
    for trial in [2 ** _ for _ in range(10, 20)]:
        m = timeit.timeit(stmt=code1, setup=setup + str([random.randint(1, 100) for _ in range(trial)]), number=1)
        xlist.append(trial)
        ylist.append(m)
        print('{0:d}\t{1:f}'.format(trial, m))

    l, = plt.plot(xlist, ylist, '--ro')
    l.set_antialiased(False)
    plt.show()

TCtime()

