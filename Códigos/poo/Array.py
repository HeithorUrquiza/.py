class Array():
    
    def __init__(self, capacity, fillValue):
        self.lyst = list()
        self.logicalSize = 0
        for count in range(capacity):
            self.lyst.append(fillValue)

    def __len__(self):
        return len(self.lyst)
    
    def size(self):
        #for i in range(self.__len__()):
           #if a.lyst[i] != None:
                #self.logicalSize += 1
        return self.logicalSize
    
    def __str__(self):
        return str(self.lyst)
 
    def __iter__(self):
        return iter(self.lyst)
    
    def __getItem__(self, index):
        if 0 <= index < self.__len__():
            return self.lyst[index]
        else:
            raise Exception("Erro no index informado")
        
    def __setItem__(self, index, newItem):
        if 0 <= index < self.__len__():
            self.lyst[index] = newItem
            self.logicalSize += 1
        else:
            raise Exception("Erro no index informado")
            
    
        
a = Array(5, None)
for i in range(a.__len__() - 2):
    value = int(input("Valor: "))
    a.__setItem__(i, value)
print(a.size())








