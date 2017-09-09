
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            #Nice recursive trick
            #Razen z addToSubTree mamy double recursion
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            self.right = self.addToSubTree(self.right, value)

    def addToSubTree(self, parent, value):
        if parent is None:
            return BinaryNode(value)

        parent.add(value)
        return parent

    def remove(self, value):
        if value < self.value:
            self.letf = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            if self.left is None:
                return self.right

            #find largest value in left subtree
            child = self.left
            while child.right:
                child = child.right

            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey

        return self

    #Własna implementacja na potrzeby def preorder()
    def isEmpty(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def removeFromParent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

    # def __repr__(self):
    #     """Useful debugging function to produce linear tree representation."""
    #     leftS = ''
    #     rightS = ''
    #     if self.left:
    #         leftS = str(self.left)
    #     if self.right:
    #         rightS = str(self.right)
    #     return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)


    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True

        return False

    def __repr__(self):
        if self.root is None:
            return 'binary: is empty'
        return 'binary' + str(self.root)

    # Własna implentacja na potrzeby metody classy BinaryTree inorder
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    # Własna impementacja  ----------- DLACZEGO NIE DZIALA ???
    # def inorder(self, node):
    #     if node.isEmpty():
    #         return
    #     self.inorder(node.left)
    #     print(node.value)
    #     self.inorder(node.right)

    def inorder(self, node):  # Już działa chodziło o różnicę isEmpty == vs is
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)



# Własna implementacja Preorder + metoda isEmpty na klasie BinaryNode
# def preorder_(parent):
#     print (parent.value)
#     if parent.isEmpty():
#         return
#     preorder(parent.left)
#     preorder(parent.right)

def preorder_(parent):

    if parent is None:
        return

    print(parent.value)
    preorder_(parent.left)
    preorder_(parent.right)


def preorder(parent):

    if parent is not None:

        print(parent.value)
        preorder(parent.left)
        preorder(parent.right)

def inorder(parent):

    if parent is not None:

        inorder(parent.left)
        print(parent.value)
        inorder(parent.right)



# ------------------------------------------------

b = BinaryTree()
b.add(5)
b.add(1)
b.add(7)
b.add(9)
b.add(8)

print('----- inorder')
inorder(b.root)
print('----- preorder')
preorder(b.root)
print('----- preorder_')
preorder_(b.root)
print('----- BinaryTree.inorder')
b.inorder(b.root)
