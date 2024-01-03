#binary tree traversal 

class Bst:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Bst(data)

root = Bst(10)
list1 = [20,5,30,40,25]
for i in list1:
    root.insert(i)