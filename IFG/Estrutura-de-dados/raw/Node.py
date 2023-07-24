class Node():
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
         
    def __repr__(self) -> str:
        r = ""
        pointer = head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
            if pointer is None:
                r = r + "None"
        return r
    
    def __str__(self):
        return self.__repr__()
    
    def showNode(self): # Representação do nó
        return self.__str__()
    
    def getIndex(self, index): # Retorna o valor com base no indice
        pointer = head
        if index >= 0:
            while index > 0:
                if pointer:
                    pointer = pointer.next
                    index -= 1
                else:
                    raise IndexError("Index out of range")
            return pointer.data
        else:
            raise IndexError("Index out of range")
        
    def getValue(self, value): # Confere se o valor está no nó
        pointer = head
        while pointer and value != pointer.data:
            pointer = pointer.next
        if pointer:
            return True
        else:
            raise ValueError(f"{value} is not in Node")
        
    def setIndex(self, index, newValue): # Altera o valor com base no índice
        pointer = head
        if index >= 0:
            while index > 0:
                if pointer:
                    pointer = pointer.next
                    index -= 1
                else:
                    raise IndexError("Index out of range")
            pointer.data = newValue
        else:
            raise IndexError("Index out of range")
        
    def setValue(self, value, newValue): # Altera o valor para um novo caso exista
        pointer = head
        while pointer and value != pointer.data:
            pointer = pointer.next
        if pointer:
            pointer.data = newValue
        else:
            raise ValueError(f"{value} is not in Node")
        
    def insertBegin(self, newItem): # Insere um valor no início
        global head
        head = Node(newItem, head)
        
    def insertEnd(self, newItem): # Insere um valor no final
        global head
        newNode = Node(newItem)
        if head is None:
            head = newNode
        else:
            pointer = head
            while pointer.next:
                pointer = pointer.next
            pointer.next = newNode
            
    def insert(self, newItem, index): # insere um valor em qualquer posição
        global head
        if self.getIndex(index):
            if head is None or index <= 0:
                head = Node(newItem, head)
            else:
                pointer = head
                while (index > 1 and pointer.next != None):
                    pointer = pointer.next
                    index -= 1
                pointer.next = Node(newItem, pointer.next)
            
    def removeBegin(self): # Remove um item do início
        global head
        removedItem = head.data
        head = head.next
        return removedItem
            
    def removeEnd(self): # Remove um item do final
        global head
        removedItem = head.data
        if head.next is None:
            head = None
        else:
            pointer = head
            while(pointer.next.next != None):                    
                pointer = pointer.next
            removedItem = pointer.next.data
            pointer.next = None
            return removedItem
        
    def remove(self, index): # Remove um item de qualquer posição
        global head
        if self.getIndex(index):
            if index <= 0 or head.next is None:
                removedItem = head.data
                head = head.next
                return removedItem
            else:
                pointer = head
                while index > 1 and pointer.next.next != None:
                    pointer = pointer.next
                    index -= 1
                removedItem = pointer.next.data
                pointer.next = pointer.next.next
                return removedItem
                

head = None
for i in range(1, 6):
    head = Node(i, head)
    
# a) print(head.showNode())
# b1) head.getIndex(0) / b2)print(head.getValue(3))
# c1) head.setIndex(3, 8) / c2) head.setValue(4, 6)
# d1) head.insertBegin(10) / d2) head.insertEnd(-1)
# e) head.insert(7, 3)
# f1) print(head.removeBegin()) / f2) print(head.removeEnd())
# g) print(head.remove(1))

print(head.showNode())
head.insertBegin(10)
head.insertEnd(-5)
print(head.showNode())
head.removeBegin()
head.removeEnd()
print(head.showNode())

