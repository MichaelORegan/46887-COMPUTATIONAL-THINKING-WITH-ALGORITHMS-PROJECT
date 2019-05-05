# Michael O'Regan 05/May/2019
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

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

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

num_runs = 10
for r in range(num_runs):
    start_time = time.time_ns()
    mergeSort(a)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsa = []
    resultsa.append(time_elapsed)
ra = round(statistics.mean(resultsa),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(b)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsb = []
    resultsb.append(time_elapsed)
rb = round(statistics.mean(resultsb),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(c)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsc = []
    resultsc.append(time_elapsed)
rc = round(statistics.mean(resultsc),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(d)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsd = []
    resultsd.append(time_elapsed)
rd = round(statistics.mean(resultsd),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(e)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultse = []
    resultse.append(time_elapsed)
re = round(statistics.mean(resultse),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(f)
    end_time = time.time_ns()
    resultsf = []
    time_elapsed = (end_time - start_time)*10**-6
    resultsf.append(time_elapsed)
rf = round(statistics.mean(resultsf),3)
for r in range(num_runs):
    np.random.seed(1)
    a = np.random.randint(1000, size=100)
    start_time = time.time_ns()
    mergeSort(g)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsg = []
    resultsg.append(time_elapsed)
rg = round(statistics.mean(resultsg),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(h)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsh = []
    resultsh.append(time_elapsed)
rh = round(statistics.mean(resultsh),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(i)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsi = []
    resultsi.append(time_elapsed)
ri = round(statistics.mean(resultsi),3)
for r in range(num_runs):
    np.random.seed(1)
    start_time = time.time_ns()
    mergeSort(j)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsj = []
    resultsj.append(time_elapsed)
rj = round(statistics.mean(resultsj),3)
for r in range(num_runs):
    np.random.seed(1)
    a = np.random.randint(1000, size=100)
    start_time = time.time_ns()
    mergeSort(k)
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsk = []
    resultsk.append(time_elapsed)
rk = round(statistics.mean(resultsk),3)

mergebench = [ra, rb, rc, rd, re, rf, rg, rh, ri, rj, rk]