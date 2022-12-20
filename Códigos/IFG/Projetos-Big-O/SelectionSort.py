from calendar import c
import time
from turtle import end_fill

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
c = 0
for i in range(465):
    c += 1
    data.append(c)
size = len(data)
start = time.time()
selectionSort(data, size)
end = time.time() - start
print("Time: {:.2f}".format(end))
