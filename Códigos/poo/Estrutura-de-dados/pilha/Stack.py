from raw import NewNode

class Stack:
    
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push(self, item): 
        # Insere um elemento na pilha
        node = NewNode.Node(item)
        node.next = self.top
        self.top = node
        self._size += 1
    
    def pop(self):
        # Remove o último elemento da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return self.top.data
        raise IndexError ("The stack is empty")
        
    def peek(self):
        # Retorna o último elemento da pilha
        if self._size > 0:
            return self.top.data
        raise IndexError ("The stack is empty")
        
    def __len__(self):
        return self._size
    
    def __repr__(self) -> str:
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(self.top.data) + "\n"
            pointer = pointer.next
        return r      
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __contains__(self, item):
        # Verifica se há respectivo valor na pilha
        pointer = self.top
        while(pointer):
            if pointer.data == item:
                return True
        raise ValueError ("This value isn't in the Stack!")
        
    
    def isEmpty(self):
        # Confere se a pilha está vazia
        if self._size == 0:
            return True
        else:
            return False