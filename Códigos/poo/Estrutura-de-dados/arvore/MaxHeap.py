class MaxHeap:
    
    def __init__(self, lyst = None):
        if lyst is None:
            self.lyst = []
            self._size = 0
        else:
            self.lyst = lyst
            self._size = len(self.lyst)


    def isEmpty(self):
        if self._size == 0:
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


    def __add__(self, other): #Refazer/analisar
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


    def pop(self): #equivale a função demote nos slides // PS: descobrir com resolver isso daq
        if self._size <= 1:
            return -1
        
        current = 1
        popped = self.lyst[1]
        self.lyst[1] = self.lyst[self._size - 1]
        self._size -= 1
        
        while((2 * current) < self._size):
            child = 0
            if (2 * current + 1) == self._size:
                child = 2 * current
            else:
                if self.lyst[2 * current] > self.lyst[2 * current + 1]:
                    child = 2 * current
                else:
                    child = 2 * current + 1
            
            if self.lyst[current] < self.lyst[child]:
                aux = self.lyst[current]
                self.lyst[current] = self.lyst[child]
                self.lyst[child] = aux
                
                current = child
            else:
                break
        return popped
        

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
    list = [None, 10, 7, 5, 4, 3]
    heap = MaxHeap(list)
    print(heap)
    heap.pop()
    print(heap)
    
    