from NewNode import Node

class LinkedList(): # classe pasa a criação de uma lista encadeada
    
    def __init__(self):
        self.head = None
        self._size = 0
        
    def __len__(self): # Retorna o tamanho da lista
        return self._size
    
    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def __getItem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError(" List index out of range")
            
        
    def append(self, newItem):
        if self.head: # Inserção caso a lista já possua elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(newItem)
        else: # Primeira inserção na lista
            self.head = Node(newItem)
        self._size += 1
        

lyst = LinkedList()
for i in range(5):
    lyst.append(int(input("Valor: ")))
print(len(lyst))
print(lyst.__getItem__(2))

