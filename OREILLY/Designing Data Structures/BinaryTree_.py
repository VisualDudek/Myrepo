
class BN:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def add(self, value):
        if value < self.value:
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            self.right = self.addToSubTree(self.right, value)
        else:
            return False

    def addToSubTree(self, parent, value):
        if parent is None:
            # parent = BN(value) // Zwróć uwage że nie chcesz tutaj przypisywać ponieważ przypisanie masz już w wywołaniu
            #                    // więc nalezy uzyć return
            return BN(value)

        parent.add(value)  # Takie wywołanie pomoże nam zadecudować czy prawo czy lewo
        return parent     # NIE ROZUMIEM po co tutaj return // Chyba po to żeby zostawić poprzednią strukturę ponieważ
                          #                                 // w wywołaniu mamy przypisanie do self.left lub .right

    def add_(self, value):
        if value < self.value:
            #Przypisz na lewo jeśli jest wolne jeśli nie to wywołaj siebie z self.left
            if self.left is None:
                self.left = BN(value)
                return True
            else:
                return self.left.add_(value)
        elif value > self.value:
            if self.right is None:
                self.right = BN(value)
                return True
            else:
                return self.right.add_(value)
        else:
            return False

class BT:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BN(value)
        else:
            self.root.add(value)

    def add_(self, value):
        if self.root is None:
            self.root = BN(value)
            return True
        else:
            return self.root.add_(value)

    def remove(self, value):
        pass

    def __contains__(self, item):
        node = self.root
        while node is not None:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            else:
                return True

        return False

def TC1():
    b = BT()
    print(b)
    print(type(b.root))
    b.add(7)
    print(b.root)
    print(b.root.value)
    print(7 in b)
    print(9 in b)

def TC2():
    # Autorska metoda add_ która zwraca True or False
    b = BT()
    print(b)
    print(b.add_(7))
    print(b.add_(8))
    print(b.add_(9))
    print(b.add_(4))
    print(b.add_(4))


# TC1()
TC2()


