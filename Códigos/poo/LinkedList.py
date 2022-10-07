from NewNode import Node

class LinkedList(): # classe pasa a criação de uma lista encadeada
    
    def __init__(self):
        self.head = None
        self._size = 0
        
    def __len__(self): # Retorna o tamanho da lista
        return self._size
    
    def _getNode(self, index): # Confere se exite algum valor no indice
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def __getitem__(self, index): # Retorna um valor da lista com base no indice
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError(" List index out of range")
        
    def __setitem__(self, index, newItem): # Altera o valor do indice
        pointer = self._getNode(index)
        if pointer:
            pointer.data = newItem
        else:
            raise IndexError("List index out of range")
        
    def __repr__(self) -> str: # Cria uma representação para a lista
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
            if pointer is None:
                r = r + "None"
        return r
    
    def __str__(self) -> str:
        return self.__repr__()
            
    def append(self, newItem):
        if self.head: # Inserção caso a lista já possua elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(newItem)
        else: # Primeira inserção na lista
            self.head = Node(newItem)
        self._size += 1
        
    def index(self, value): # Confere se o valor existe na lista
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.data == value:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{value} is not in list")
        

# Testes das funções/Métodos
lyst = LinkedList()
lyst.append(3)
lyst.append(7)
lyst.append(10)
lyst.append(2)
lyst.append(-1)
lyst.append(20)
print(lyst)
print(lyst[4])
lyst[4] = 100
print(lyst)
print(lyst.index(20))
print(len(lyst))


