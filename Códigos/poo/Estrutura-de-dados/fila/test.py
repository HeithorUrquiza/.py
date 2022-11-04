from Queue import Queue

queue = Queue()
queue.push(10)
queue.push('Heithor')
queue.push(False)
queue.push(7.8)
queue.push(0)
print(queue)
queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.pop()
print(queue)
print(queue.peek())

''' ----------------------------------------- 
Teste Queue com lista python

from ListQueue import Queue

queue = Queue()
queue.push(10)
queue.push(5)
queue.push(8)
queue.push(11)
queue.push(78)
print(queue)
print(queue.peek())
queue.pop()
queue.pop()
print(queue)
print(queue.peek())
queue.pop()
queue.pop()
queue.pop()
print(queue.isEmpty())
'''
