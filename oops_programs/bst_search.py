class Bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Bst(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")
    
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
           self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)

     #performing delete operation
    def delete(self,data):
        if self.key is None:
            print("Node is empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("node is not present")
        elif data>self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while self.lchild:
                node=self.lchild
            self.key = node.key
            self.rchild=self.rchild.delete(node.key)
        return self

        

root = Bst(10)
list1 = [6,3,1,6,8,7,12]
for i in list1:
    root.insert(i)
print("Preorder")
root.preorder()
root.delete(6)