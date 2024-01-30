# https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
        return self.root is not None
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return node

tree = BinarySearchTree()
keys = sys.stdin.readlines()
for key in keys:
    tree.insert(int(key))

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key)
    
postorder(tree.root)