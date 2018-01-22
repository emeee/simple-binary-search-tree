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

class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self, key, val):
        if self.root:
            self._insert(key, val, self.root)
        else:
            self.root = Node(key ,val)
        self.size = self.size + 1

    def _insert(self, key, val, currentNode):
        if key < currentNode.getKey():
            if currentNode.getLeftChild():
                self._insert(key, val, currentNode.getLeftChild(), parent=currentNode)
            else:
                currentNode.setLeftChild(Node(key, val))
        else:
            if currentNode.getRightChild():
                self._insert(key, val, currentNode.getRightChild(), parent=currentNode)
            else:
                currentNode.setRightChild(Node(key, val))

    def get(self, key):
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key < currentNode.getKey():
            return self._get(key, currentNode.getLeftChild())
        elif key > currentNode.getKey():
            return self._get(key, currentNode.getRightChild())
        elif key == currentNode.getKey():
            return currentNode

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._delete(nodeToRemove)
                self.size = self.size - 1
            else:
                raise('Key not found')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise('Empty tree')

    def _delete(self, key, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.getLeftChild():
                currentNode.parent.setLeftChild = None
            else:
                currentNode.parent.setRightChild = None
        #TODO: Other cases
