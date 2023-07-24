from Node import Node

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
        
    def __len__(self):
        return self._size()
    
    
    def __repr__(self) -> str:
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + "  "
                pointer = pointer.next
            return r
        else:
            return "Empty queue !!"
    
    
    def __str__(self) -> str:
        return self.__repr__()
    
    
    def push(self, item):
        # Insere um elemento na pilha
        node = Node(item)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        if self.first is None:
            self.first = node
            
        self._size += 1
    
    
    def pop(self):
        # Remove o primeiro item da fila
        if self.first is not None:
            item = self.first.data
            self.first = self.first.next
            self._size -= 1
            return item
        else:
            raise IndexError("The Queue is empty")
    
    
    def peek(self):
        # Retorna o primeiro item da fila sem excluir
        if self.first is not None:
            return self.first.data
        else:
            raise IndexError("The Queue is empty")
        
        
    def isEmpty(self):
        # Verifica se a lista está vazia
        if (self.first and self._size != 0):
            return False
        else:
            return True
