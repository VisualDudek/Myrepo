
class BN:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BN(value)
                return True
            else:
                return self.right.add(value) # UWAGA do przemyslenia
        elif value < self.value:
            if self.left is None:
                self.left = BN(value)
                return True
            else:
                return self.left.add(value)  # UWAGA do przemyslenia
        else:
            return False

    def getList(self):
        left_list = [] if self.left is None else self.left.getList()
        right_list = [] if self.right is None else self.right.getList()
        return left_list + [self.value] + right_list


class BT:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BN(value)
            return True
        else:
            return self.root.add(value) # UWAGA 1) wykonasie stm. a porem zwróce wynik

    def __repr__(self):
        if self.root is not None:
            return 'BinartTree: ' + ','.join(map(str,self.root.getList()))

    # def __repr__(self):   ZOBACZ DLACZEGO NIE BEDZIE DZIALAC I DLACZEGO TRZEBA UZYWAC  return a nie print
    #     if self.root is not None:
    #         print('BinartTree: ' + ','.join(map(str,self.root.getList() )))


print(__name__)

def TC1():
    b = BT()
    b.add(5)
    b.add(8)
    b.add(3)
    b.add(9)

def TC2():
    b = BT()
    b.add(5)
    b.add(8)
    b.add(3)
    b.add(9)
    print(b)

if __name__ == '__main__':
    TC2()
    # TC1()
