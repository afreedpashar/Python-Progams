class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

    def preOrder(root):
        if root!=None:
            print(root.key)
            preOrder(root.left)
            preOrder(root.right)

#driver code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right=Node(50)

preOrder(root)
        