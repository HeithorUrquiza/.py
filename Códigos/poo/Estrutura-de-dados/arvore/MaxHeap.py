import sys

class MaxHeap:
    
    def __init__(self, lyst = None):
        if lyst is None:
            self.lyst = []
            self._size = 0
        else:
            self.lyst = lyst
            self._size = len(self.lyst)


    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    
    def __len__(self):
        return self._size
    
    
    def __iter__(self):
        return iter(self.lyst)
    
    
    def __str__(self):
        return str(self.lyst)


    def __contains__(self, item):
        for value in self.lyst:
            if item == value:
                return True
        return False


    def __add__(self, other):
        if type(self) == type(other):
            for item in other:
                self.push(item)


    def __eq__(self, other):
        if type(self) == type(other):
            return True
        else:
            return False


    def peek(self):
        return self.lyst[1]


    def push(self, item): #equivale a função promote nos slides
        self.lyst.append(item)
        i = len(self.lyst) - 1
        while i > 0:
            parentIndex = i//2
            parentItem = self.lyst[parentIndex]
            # Elemento chegou na raiz da árvore
            if parentItem == None or parentItem >= item:
                break
            else:
                self.lyst[i] = self.lyst[parentIndex]
                self.lyst[parentIndex] = item
                i = parentIndex
        self._size += 1


    def pop(self): #equivale a função demote nos slides
        if self._size < 1:
            print("Não há raiz")
            return None
        aux = self.lyst[1]
        self.lyst[1] = self.lyst[-1]
        self.lyst[-1] = aux
        
        self.lyst.pop(len(self.lyst) - 1)
        self._size -= 1
        
        position = 1
        while(True):
            if self.left_child(position) != None and self.right_child(position) != None:
                if (self.left_child(position) > self.lyst[position]) and (self.left_child(position) > self.right_child(position)):
                    aux = self.left_child(position)
                    self.lyst[2 * position] = self.lyst[position]
                    self.lyst[position] = aux
                if(self.left_child(position) != None and self.right_child(position) != None):
                    if (self.right_child(position) > self.lyst[position]) and (self.right_child(position) > self.left_child(position)):
                        aux = self.right_child(position)
                        self.lyst[2 * position + 1] = self.lyst[position]
                        self.lyst[position] = aux
            elif self.left_child(position) != None:
                if self.left_child(position) > self.lyst[position]:
                    aux = self.left_child(position)
                    self.lyst[2 * position] = self.lyst[position]
                    self.lyst[position] = aux
            elif self.right_child(position) != None:
                if self.right_child(position) > self.lyst[position]:
                    aux = self.right_child(position)
                    self.lyst[2 * position + 1] = self.lyst[position]
                    self.lyst[position] = aux
            elif self.right_child(position) is None and self.left_child(position) is None:
                return
            position += 1
            if self.right_child(position) is None and self.left_child(position) is None:
                return
            elif self.right_child(position) != None and self.left_child(position) is None:
                if self.right_child(position) < self.lyst[position]:
                    return
            elif self.right_child(position) is None and self.left_child(position) != None:
                if self.left_child(position) < self.lyst[position]:
                    return
        

    def min_item(self):
        minItem = self.lyst[-1]
        for i in self.lyst:
            if(i != None and minItem > i):
                minItem = i
        return minItem


    def left_child(self, index):
        return self.lyst[2 * index]


    def right_child(self, index):
        return self.lyst[(2 * index) + 1]


    def parent(self, index):
        return self.lyst[index//2]
    
    
if __name__ == "__main__":
    list = [None, 18, 14, 15, 9, 8, 4, 6]
    a = MaxHeap(list)
    print(a.parent(3))
    
    