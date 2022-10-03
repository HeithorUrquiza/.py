import time
problemSize = 36
print("%12s%16s" %("ProblemSize", "Seconds"))
for count in range(problemSize):
    start = time.time()
    work = 1
    for k in range(problemSize):
        work+=1
        for j in range(problemSize):
            work -= 1
            for l in range(problemSize):
                work += 1
                work -= 1
    elapsed = time.time() - start
    print("%12d%16.2f" % (problemSize, elapsed))
    problemSize*= 2