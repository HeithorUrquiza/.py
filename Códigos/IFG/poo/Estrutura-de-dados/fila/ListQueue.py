class Queue:
  
  def __init__(self):
    self.queue = []
    self._size = 0
    
  
  def __len__(self):
    return self._size()


  def __repr__(self):
    if self.queue:
      r = ""
      i = 0
      while i <= len(self.queue) - 1:
        r = r + str(self.queue[i]) + " "
        i += 1
      return r
    else:
      return "Empty queue!!"
    

  def __str__(self):
    return self.__repr__()
    
    
  def isEmpty(self):
    # Verifica se a lista está vazia
    if (self.queue and self._size != 0):
      return False
    else:
      return True
    

  def push(self, item):
    # Adiciona um item ao final da fila
    self.queue.append(item)
    self._size += 1
    

  def pop(self):
    # Remove o primeiro item da fila
    if self.queue:
      self.queue.pop(0)
      self._size -= 1
    else:
      raise IndexError("The Queue is empty")

    
  def peek(self):
    # Retorna o primeiro item sem excluí-lo
    if self.queue:
      return self.queue[0]
    else:
      raise ValueError("The Queue is empty")

  