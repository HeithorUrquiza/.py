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
    
    def insert(self, index, newElem):# Insere um elemento em qualquer poisção
        node = Node(newElem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1
    
    def remove(self, elem):
        if self.head is None:
            raise ValueError(f"{elem} isn't in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError(f"{elem} isn't in list")
        

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
lyst.insert(3, 30)
print(lyst)
print(lyst.remove(30))
print(lyst)


