from node import Node

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
        self.size += 1

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
                self.size -= 1
            else:
                raise('Key not found')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise('Empty tree')

    def _delete(self, key, currentNode):
        #Simple delete
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.getLeftChild():
                currentNode.parent.setLeftChild = None
            else:
                currentNode.parent.setRightChild = None
        #Replace de node with its child
        if currentNode.hasOneChild():
            if currentNode.getLeftChild():
                if currentNode.parent.getLeftChild() == currentNode:
                    currentNode.parent.setLeftChild(currentNode.getLeftChild())
                else:
                    currentNode.parent.setRightChild(currentNode.getLeftChild())
            else:
                if currentNode.parent.getLeftChild() == currentNode:
                    currentNode.parent.setLeftChild(currentNode.getRightChild())
                else:
                    currentNode.parent.setRightChild(currentNode.getRightChild())
        #TODO: HasTwoChild


    def printPreOrder(self, node):
        if node is not None:
            print node.data
            self.printPreOrder(node.left)
            self.printPreOrder(node.left)

    def printInOrder(self, node):
        if node is not None:
            self.printPreOrder(node.left)
            print node.data
            self.printPreOrder(node.left)

    def printInOrder(self, node):
        if node is not None:
            self.printPreOrder(node.left)
            self.printPreOrder(node.left)
            print node.data
