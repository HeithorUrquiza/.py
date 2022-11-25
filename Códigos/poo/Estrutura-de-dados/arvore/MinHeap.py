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
        
        if (self.lyst[1] > self.lyst[-1]):
            aux = self.lyst[1]
            self.lyst[1] = self.lyst[-1]
            self.lyst[-1] = aux
        
        i = 1
        while True:
            leftChild = 2 * i
            rightChild = 2 * i + 1
            
            if leftChild > len(self.lyst) - 1:
                break
            elif self.lyst[i] != None: 
                if self.lyst[leftChild] != None and self.lyst[i] > self.lyst[leftChild]: 
                    aux = self.lyst[i]
                    self.lyst[i] = self.lyst[leftChild]
                    self.lyst[leftChild] = aux
            
            if rightChild > len(self.lyst) - 1:
                break
            elif self.lyst[i] != None:
                if self.lyst[rightChild] != None and self.lyst[i] > self.lyst[rightChild]:
                    aux = self.lyst[i]
                    self.lyst[i] = self.lyst[rightChild]
                    self.lyst[rightChild] = aux
                    
            i+=1
            '''indexParent = i//2
            leftChild = 2 * indexParent
            rightChild = 2 * indexParent + 1
            
            if self.lyst[indexParent] != None: 
                if self.lyst[leftChild] != None and self.lyst[indexParent] > self.lyst[leftChild]: 
                    aux = self.lyst[indexParent]
                    self.lyst[indexParent] = self.lyst[leftChild]
                    self.lyst[leftChild] = aux
            
            if self.lyst[indexParent] != None:
                if rightChild == i and self.lyst[indexParent] > self.lyst[rightChild]:
                    aux = self.lyst[indexParent]
                    self.lyst[indexParent] = self.lyst[rightChild]
                    self.lyst[rightChild] = aux'''
            
            self._size += 1
        

    def pop(self): #equivale a função demote nos slides
        if self.isEmpty():
            raise AttributeError("Min heap is empty")
        
        root = self.lyst[1]
        lastItem = self.lyst[-1]
        self.lyst[1] = lastItem
        self.lyst.pop(-1)
        
        i = 1
        while True:
            leftChild = 2 * i
            rightChild = 2 * i + 1
            
            if leftChild > len(self.lyst) - 1: 
                break
            elif self.lyst[i] != None: 
                if self.lyst[leftChild] != None and self.lyst[i] > self.lyst[leftChild]: 
                    aux = self.lyst[i]
                    self.lyst[i] = self.lyst[leftChild]
                    self.lyst[leftChild] = aux
            
            if rightChild > len(self.lyst) - 1:
                break
            elif self.lyst[i] != None:
                if self.lyst[rightChild] != None and self.lyst[i] > self.lyst[rightChild]:
                    aux = self.lyst[i]
                    self.lyst[i] = self.lyst[rightChild]
                    self.lyst[rightChild] = aux
                    
            i+=1
            
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
    list = [None, 1, 3, 2, 7]
    heap = MinHeap(list)
    heap.push(4)
    heap.push(0)
    heap.push(-1)
    print(heap)
    heap.pop()
    heap.pop()
    heap.pop()
    print(heap)
    print(heap.max_item())