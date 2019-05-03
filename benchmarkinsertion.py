# Michael O'Regan 03/May/2019
# https://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

import time
import statistics
import numpy as np                              # importing numpy as np

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

def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

num_runs = 10
for r in range(num_runs):
    start_time = time.time_ns()
    insertionSort(a)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsa = []
    resultsa.append(time_elapsed)
ra = round(statistics.mean(resultsa),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(b)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsb = []
    resultsb.append(time_elapsed)
rb = round(statistics.mean(resultsb),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(c)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsc = []
    resultsc.append(time_elapsed)
rc = round(statistics.mean(resultsc),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(d)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsd = []
    resultsd.append(time_elapsed)
rd = round(statistics.mean(resultsd),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(e)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultse = []
    resultse.append(time_elapsed)
re = round(statistics.mean(resultse),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(f)
    end_time = time.time_ns()
    resultsf = []
    time_elapsed = (end_time - start_time)*10**-6
    resultsf.append(time_elapsed)
rf = round(statistics.mean(resultsf),3)
for r in range(num_runs):
    np.random.seed(1)
    a = np.random.randint(1000, size=100)
    start_time = time.time_ns()
    insertionSort(g)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsg = []
    resultsg.append(time_elapsed)
rg = round(statistics.mean(resultsg),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(h)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsh = []
    resultsh.append(time_elapsed)
rh = round(statistics.mean(resultsh),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(i)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsi = []
    resultsi.append(time_elapsed)
ri = round(statistics.mean(resultsi),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    insertionSort(j)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsj = []
    resultsj.append(time_elapsed)
rj = round(statistics.mean(resultsj),3)
for r in range(num_runs):
    np.random.seed(1)
    a = np.random.randint(1000, size=100)
    start_time = time.time_ns()
    insertionSort(k)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsk = []
    resultsk.append(time_elapsed)
rk = round(statistics.mean(resultsk),3)

insertionbench = [ra, rb, rc, rd, re, rf, rg, rh, ri, rj, rk]