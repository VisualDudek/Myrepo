class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None]*size
        self.count = 0
        self.start = 0
        self.end = 0

    def add(self, value):
        #  Znajdz bład
        # ------------------
        # if self.isFull():
        #     self.start = (self.start+1) % self.size
        #
        # self.buffer[self.end] = value
        # self.end = (self.end+1) % self.size
        # self.count += 1
        # ------------------
        # Jesli cb jest pełny to nie zwiększamy licznika !!!

        if self.isFull():
            self.start = (self.start+1) % self.size
        else:
            self.count += 1

        self.buffer[self.end] = value
        self.end = (self.end+1) % self.size

    def remove(self):
        # Usuwa i zwraca lewy element czyli koleka FIFO
        if self.isEmpty():
            raise Exception('cb jest juz pusty')
        #     Zauważ że nie potrzebujesz else:
        self.count -= 1
        value = self.buffer[self.start]
        self.start = (self.start+1) % self.size
        return value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __repr__(self):
        if self.isEmpty():
            return 'cb:[]'
        else:
            # return 'cb:[' + ','.join(map(str,self.buffer)) + ']'
            # Można odwołać się do samego self ale trzeba zapewnić iterable
            # Ciekawe robi wciecia na lamanym stringu
            return 'cb:[' + ','.join(map(str, self)) + ']' + '''
            self.start: {}
            self.end: {}
            self.count: {}
            self.buffer: {}
            '''.format(self.start, self.end, self.count, self.buffer)

    def __iter__(self):
        # Ksiązkowe uproszczone przez modyfikacje petki while -> nie potrzebne var num
        # jednak błąd, patrz poniżej
        #
        # idx = self.start
        # num = self.count
        # while num > 0:
        #     yield self.buffer[idx]
        #     idx = (idx+1) % self.size
        #     num -= 1

        #  Przeoczyłes fakt ze przy pelnym cb start = end
        # idx = self.start
        # while idx != self.end:
        #     yield self.buffer[idx]
        #     idx = (idx+1) % self.size

        idx = self.start
        for _ in range(self.count):
            yield self.buffer[idx]
            idx = (idx+1) % self.size


c = CircularBuffer(3)
print(c)
c.add(3)
c.add(4)
c.add(5)
c.add(6)
print(c)
print(c.remove())

class MovingAverage(CircularBuffer):

    def __init__(self, size):
        CircularBuffer.__init__(self, size)
        self.total = 0

    def getAverage(self):
        if self.count == 0:
            return 0
        return self.total / self.count

    def add(self, value):
        if self.isFull():
            delta = -self.buffer[self.start]
        else:
            delta = 0
        delta += value
        self.total += delta
        CircularBuffer.add(self, value)

    def remove(self):                      # Teraz wiadomo dlaczego przydaje sie return w CB.remove
        removed = CircularBuffer.remove(self)    #Dlaczego musze tutaj przekazywac argument self???
        self.total -= removed
        return removed

    def __repr__(self):
        if self.isEmpty():
            return 'ma:[]'

        return 'ma:[' + ','.join(map(str,self)) + ']:' + str(self.getAverage())

