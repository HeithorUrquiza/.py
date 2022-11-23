class MinHeap:

    def __init__(self, lyst=None):
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
        i = self._size
        stop = False
        while (i//2 > 0) and stop == False:
            if self.lyst[i] < self.lyst[i//2]:
                self.lyst[i], self.lyst[i//2] = self.lyst[i//2], self.lyst[i]
            else:
                stop = True
            i = i//2
        self._size += 1
        

    def pop(self): #equivale a função demote nos slides
        if self.isEmpty():
            raise AttributeError("Min heap is empty")
        
        root = self.lyst[1]
        self.lyst[1] = self.lyst[-1]
        self.lyst.pop(-1)
        
        i = 1
        while (i * 2) <= self._size:
            minChild = 0
            if (i * 2) + 1 > self._size:
                minChild = i * 2
            else:
                if self.lyst[i * 2] < self.lyst[(i * 2) + 1]:
                    minChild = i * 2
                else:
                    minChild = (i * 2) + 1
            
            if self.lyst[i] > self.lyst[minChild]:
                self.lyst[i], self.lyst[minChild] = self.lyst[minChild], self.lyst[i]
            i = minChild
        self._size -= 1
        return root

    
    def max_item(self):
        maxItem = self.lyst[-1]
        for i in self.lyst:
            if(i != None and maxItem < i):
                maxItem = i
        return maxItem
    
    
    def left_child(self, index):
        return self.lyst[2 * index]
        
        
    def right_child(self, index):
        return self.lyst[(2 * index) + 1]


    def parent(self, index):
        return self.lyst[index//2]
    
  
    
if __name__ == "__main__":
    list = [None, 2, 7, 9, 1]
    heap = MinHeap(list)
    heap.pop()
    print(heap)