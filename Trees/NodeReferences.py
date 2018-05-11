class BinaryTree:
    def __init__(self,rootobj):
        self.key = rootobj
        self.left = None
        self.right = None


    def insertLeft(self,newNode):
        if self.left==None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

#
# r = BinaryTree(0)
#
# r.insertLeft(1)
#
# r.insertRight(2)
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())