import random

ROOT = 'root'

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
        
        
class BinaryTree:
    def __init__(self, data = None, node = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
        
    # Percurso em Pós-Ordem
    def posOrder_percussion(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.posOrder_percussion(node.left)
        if node.right:
            self.posOrder_percussion(node.right)
        print(node, end = ' ')
        
    # Percurso em IN-Ordem
    def inOrder_percussion(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.inOrder_percussion(node.left)
        print(node, end = ' ')
        if node.right:
            self.inOrder_percussion(node.right)
            
    # Percurso em Pré-Ordem
    def preOrder_percussion(self, node = None):
        if node is None:
            node = self.root
        print(node, end = ' ')
        if node.left:
            self.preOrder_percussion(node.left)
        if node.right:
            self.preOrder_percussion(node.right)
            
    # Altura da árvore
    def height(self, node = None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright
        return hleft
    
    
class BinarySearchTree(BinaryTree):
    #Inserção de valores na árvore
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
            
    #Pesquisa de valores na árvore
    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node is None:
            return None
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)
            
        
if __name__ == "__main__":
    random.seed(80)
    
    values = random.sample(range(1, 1000), 30)
    
    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)
        
    bst.inOrder_percussion()
    
    items = [26, 399, 780, 888]
    print('\n')
    for item in items:
        r = bst.search(item)
        if r is None:
            print(item, 'não encontrado')
        else:
            print(r.root.data, ' encontrado')
    
    