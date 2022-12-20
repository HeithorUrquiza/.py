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
        i = len(self.lyst) - 1
        while i > 0:
            indexParent = i//2
            
            if self.lyst[indexParent] != None and item > self.lyst[indexParent]:
                self.lyst[i] = self.lyst[indexParent]
                self.lyst[indexParent] = item
            else:
                break
            i = indexParent
        self._size += 1


    def pop(self): #equivale a função demote nos slides [None, 3, 2, 7]
        if self.isEmpty():
            raise AttributeError("Max Heap is empty")
        
        root = self.lyst[1]
        lastItem = self.lyst[-1]
        self.lyst[1] = lastItem
        self.lyst.pop(-1)
        
        i = 1
        lastIndex = len(self.lyst) - 1
        
        while True:
            leftIndex = 2 * i
            rightIndex = 2 * i + 1
            if lastIndex > rightIndex:
                if self.lyst[leftIndex] >= self.lyst[rightIndex]:
                    if lastItem < self.lyst[leftIndex]:
                        self.lyst[i] = self.lyst[leftIndex]
                        self.lyst[leftIndex] = lastItem
                        i = leftIndex
                    else:
                        self._size -= 1
                        return root
                else:
                    if lastItem < self.lyst[rightIndex]:
                        self.lyst[i] = self.lyst[rightIndex]
                        self.lyst[rightIndex] = lastItem
                        i = rightIndex
                    else:
                        self._size -= 1
                        return root
            else:
                if lastIndex >= leftIndex:
                    if lastItem < self.lyst[leftIndex]:
                        self.lyst[i] = self.lyst[leftIndex]
                        self.lyst[leftIndex] = lastItem
                        
                self._size -= 1
                return root

    def min_item(self):
        minItem = self.lyst[-1]
        for i in self.lyst:
            if(i != None and minItem > i):
                minItem = i
        return minItem


    def left_child(self, index):
        if 2 * index > len(self.lyst) - 1:
            return IndexError("This child is empty")
        else:
            return self.lyst[2 * index]


    def right_child(self, index):
        if (2 * index) + 1 > len(self.lyst) - 1:
            return IndexError("This child is empty")
        else:
            return self.lyst[(2 * index) + 1]


    def parent(self, index):
        return self.lyst[index//2]
    
    
if __name__ == "__main__":
    list = [None, 10, 7, 5, 4, 3]
    heap = MaxHeap(list)
    heap.push(9)
    print(heap)
    heap.pop()
    print(heap)
    print(heap.left_child(3))
    print(heap.right_child(3))
    print(heap.parent(3))
    print(heap.peek())
    print(0 in heap)
    print(heap.isEmpty())
    
    