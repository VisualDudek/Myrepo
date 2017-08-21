
# Link List
from collections import deque

class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

class LinkedList:
    # struktura odzwierciedla stos LIFO
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        # Add value to the front of the list. O(1)
        self.head = LinkedNode(value, self.head)

    def remove(self, value):
        n = self.head
        last = None

        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True

            last = n
            n = n.next
        return False

    def pop(self):
        # Remove first value from DS
        if self.head is None:
            raise Exception ('Empty DS')
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head == None:
            return 'link:[]'

        return 'link:[' + ','.join(map(str,self)) + ']'

class QueueLinkedList:
    def __init__(self, *start):
        self.head = None
        self.tail = None

        for _ in start:
            self.append(_)

    def append(self, value):
        # Add value to the END of the list. O(1)
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, value):
        n = self.head
        last = None

        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True

            last = n
            n = n.next
        return False

    def pop(self):
        # Remove first value from DS
        if self.head is None:
            raise Exception ('Empty DS')
        val = self.head.value
        self.head = self.head.next
        if self.head is None:           #Dodatkowy bezpiecznik-check
            self.tail = None
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head == None:
            return 'queuelink:[]'

        return 'queuelink:[' + ','.join(map(str,self)) + ']'

print('----------------------')    # Example for collections.deque

d = deque('Marcin')
print(d)
d.append('Z')
d.appendleft('A')
print(d)


a = LinkedList()
print(a)
a.prepend(1)
a.prepend(2)
a.prepend(3)
print(a)
a.pop()
print(a)
print('------------')
q = QueueLinkedList()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.pop())
print(q)



