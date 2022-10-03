import time
problemSize = 1000
print("%12s%16s" %("ProblemSize", "Seconds"))

work = 0
for count in range(problemSize):
    start = time.time()
    work += 1
    work -= 1
    elapsed = time.time() - start
    print("%12d%16.2f" % (problemSize, elapsed))
    problemSize *= 2
    if problemSize >= 100000000000000000000000000000:
        break
  
  
'''import time
problemSize = 10500
print("%12s%16s" %("ProblemSize", "Seconds"))
for count in range(problemSize):
    start = time.time()
    work = 1
    for k in range(problemSize):
        work+=1
        work-=1
    elapsed = time.time() - start
    print("%12d%16.2f" % (problemSize, elapsed))
    problemSize*= 2'''



