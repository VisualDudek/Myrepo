
class BN:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BN(value)
                return True
            else:
                return self.right.add(value)
        elif value < self.value:
            if self.left is None:
                self.left = BN(value)
                return True
            else:
                return self.left.add(value)
        else:
            return False

    def getList(self):
        leftS, rightS = '', ''
        if self.left is not None:
            leftS = str(self.left.getList())
        if self.right is not None:
            rightS = str(self.right.getList())

        return rightS + ' ' + str(self.value) + ' ' + leftS

    def inorder(self):
        if self.left is not None:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right is not None:
            for v in self.right.inorder():
                yield v


class BT:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BN(value)
        else:
            return self.root.add(value)

    def __repr__(self):
        if self.root is None:
            return 'BT is empty'
        else:
            return 'BT: ' + self.root.getList()

        #  DLACZEGO TO NIE DZIALA ???
        # for _ in self.root.inorder():
        #     print(_)

    def __iter__(self):
        if self.root is not None:
            for e in self.root.inorder():
                yield e


def TC1():
    b = BT()
    b.add(5)
    b.add(6)
    b.add(7)
    b.add(3)
    print(b.root.value)
    print(b.root.right.value)
    print(b.root.left.value)

def TC2():
    b = BT()
    b.add(5)
    b.add(6)
    b.add(7)
    b.add(3)
    for _ in b:
        print(_)


TC2()