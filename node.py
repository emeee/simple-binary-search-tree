class Node:

    def __init__(self, key, val, leftChild=None, rightChild=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def getVal(self):
        return self.val

    def getKey(self):
        return self.key

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent

    def setVal(self, val):
        self.val = val

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def setParent(self, parent):
        self.parent = parent

    def isLeaf(self):
        return not(self.rightChild or self.leftChild)

    def hasTwoChild(self):
        return self.leftChild and self.rightChild

    def hasOneChild(self):
        return not(self.isLeaf() or self.hasTwoChild())
