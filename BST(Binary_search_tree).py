class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()

    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightchild:
                self.rightchild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            print(str(self.value))
            if self.rightchild:
                self.rightchild.postorder()
            
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def inorder(self):
        print("Inorder")
        self.root.inorder()

bst = Tree()
bst.insert(10)
print(bst.insert(15))
print(bst.insert(9))
print("-------------")
bst.preorder()
bst.postorder()
bst.inorder()
