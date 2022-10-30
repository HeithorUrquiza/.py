class ListStack():
    
    def __init__(self):
        self.stack = []
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def clear(self): # Limpa todos os itens da lista
        self.stack.clear()
        self._size = 0
    
    def isEmpty(self): # Confere se a pilha está vazia
        if(self.stack and self._size != 0):
            return False
        else:
            return True
    
    def __repr__(self):
        if self.stack:
            r = ""
            i = len(self.stack) - 1
            while i >= 0:
                r = r + str(self.stack[i]) + "\n"
                i -= 1
            return r
        else:
            return "[...]"
    
    def __str__(self):
        return self.__repr__()
    
    def __contains__(self):
        pass
    
    def __add__(self):
        pass
    
    def __eq__(self, __o: object) -> bool:
        pass
    
    def push(self, elem): # Adiciona um item à pilha
        self.stack.append(elem)
        self._size += 1
    
    def pop(self): # Remove o último item da pilha
        if self.stack:
            self.stack.pop()
            self._size -= 1
        else:
            raise IndexError("The stack is empty")
    
    def peek(self): # retorna o último item da pilha
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("The stack is empty")
        
        
stack = ListStack()
stack.push(1)
stack.push(10)
stack.push(20)
stack.push(-3)
print(stack)
print(len(stack))
stack.clear()
print(len(stack))

    
    