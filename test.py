# Michael O'Regan 05/May/2019
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheheapSort.html

import time
import statistics
import numpy as np  # importing numpy as np

np.random.seed(1)                                # seeding random on seed 1 so that all the arrays are the same

a = np.random.randint(200000, size=100)          # array of size 100
b = np.random.randint(200000, size=250)          # array of size 250
c = np.random.randint(200000, size=500)          # array of size 500
d = np.random.randint(200000, size=750)          # array of size 750
e = np.random.randint(200000, size=1000)         # array of size 1000
f = np.random.randint(200000, size=2500)         # array of size 2500
g = np.random.randint(200000, size=5000)         # array of size 5000
h = np.random.randint(200000, size=7500)         # array of size 7500
i = np.random.randint(200000, size=10000)        # array of size 10000
j = np.random.randint(200000, size=20000)        # array of size 20000
k = np.random.randint(200000, size=50000)        # array of size 50000

def heapify(alist, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and alist[i] < alist[l]:
        largest = l
    if r < n and alist[largest] < alist[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        alist[i],alist[largest] = alist[largest],alist[i]
        heapify(alist, n, largest)
def heapSort(alist):
    n = len(alist)
    # Build max heap
    for i in range(n, 0, -1):
        heapify(alist, n, i)
    for i in range(n-1, 0, -1):
        # swap
        alist[i], alist[0] = alist[0], alist[i]  
        #heapify root element
        heapify(alist, i, 0)

num_runs = 2
resultsa = []
for r in range(num_runs):
    np.random.seed(1)
    a = np.random.randint(200000, size=100)   
    print(a)
    start_time = time.time_ns()
    heapSort(a)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    print(a)    
    resultsa.append(time_elapsed)
ra = round(statistics.mean(resultsa),3)
print(ra)
print(resultsa)