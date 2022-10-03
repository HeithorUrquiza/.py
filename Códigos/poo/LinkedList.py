from Node import Node

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # Primeira inserção
           self.head = Node(elem)
        self._size = self._size + 1
        
    def __len__(self):
        # Retorna o tamanho da lista
        return self._size
    
    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer
    
    def __getItem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
        
    def __setItem__(self, index, elem):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
    # Retorna o indíce do elemento na lista
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.nexti 
            i = i + 1
        raise ValueError("{} is not in list".format(elem))
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
        
    def remove(self, elem):
        if self.head == None:
            raise ValueError ("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    #remove
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1 
            return True
        raise ValueError("{} is not in list".format(elem))
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
                
            
lyst = LinkedList()
lyst.append(7)
lyst.append(80)
lyst.append(56)
lyst.append(32)
lyst.append(17)
lyst.insert(0, 22)
print(lyst)
lyst.remove(80)
print(lyst)
print(len(lyst))

'''def __init__(self, data, next):
    self.data = data
    self.next = next'''
        
# Retorna o item pelo index
# Considera 0 <= index < n
'''def getIndex(self, index):
     probe = self.head
     while index > 0:
        probe = probe.next
        index -= 1
    return probe.data
    
    def show(self):
        probe = head
        while probe != None:
            print(probe.data)
            probe = probe.next'''
        
'''head = None
for i in range(1, 6):
    head = Node(i, head)
    
head.show()'''