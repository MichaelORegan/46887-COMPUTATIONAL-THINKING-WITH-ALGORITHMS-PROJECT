# Michael O'Regan 05/May/2019
# http://interactivepython.org/runestone/static/pythonds/SortSearch/ThebucketSort.html

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
j = np.random.randint(200000, size=15000)        # array of size 15000
k = np.random.randint(200000, size=20000)        # array of size 20000
l = np.random.randint(200000, size=30000)        # array of size 30000
m = np.random.randint(200000, size=50000)        # array of size 50000

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
    for i in range(length):
        insertionSort(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i] 
    return result

def insertionSort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

num_runs = 10                                       # set the benchamrk number of runs at 10
for r in range(num_runs):                           # looping the timing of the algorithm for num_runs
    np.random.seed(1)                               # setting the random seed (1)
    a = np.random.randint(200000, size=100)         # array of size 100
    start_time = time.time_ns()                     # setting start time to the time now in nanoseconds, https://docs.python.org/3/library/time.html#time.time
    bucketSort(a)                                   # calling algorithm for array a
    end_time = time.time_ns()                       # setting end time to the time now in nanoseconds
    time_elapsed = (end_time - start_time)*10**-6   # setting time elapsed to the difference of start and end to get the length of the running time of the algorithm
    resultsa = []                                   # setting results a to an empty array to fill with results
    resultsa.append(time_elapsed)                   # append the results array ie fill the results array with results of the runs as per num runs
ra = round(statistics.mean(resultsa),3)             # setting ra to the mean of results rounded to 3 decimal places https://www.geeksforgeeks.org/python-statistics-mean-function/
for r in range(num_runs):
    np.random.seed(1)
    b = np.random.randint(200000, size=250)          # array of size 250
    start_time = time.time_ns()
    bucketSort(b)                                    # calling algorithm for array b
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsb = []
    resultsb.append(time_elapsed)
rb = round(statistics.mean(resultsb),3)              # setting rb to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    c = np.random.randint(200000, size=500)          # array of size 500
    start_time = time.time_ns()
    bucketSort(c)                                    # calling algorithm for array c
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsc = []
    resultsc.append(time_elapsed)
rc = round(statistics.mean(resultsc),3)              # setting rc to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    d = np.random.randint(200000, size=750)          # array of size 750
    start_time = time.time_ns()
    bucketSort(d)                                    # calling algorithm for array d
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsd = []
    resultsd.append(time_elapsed)
rd = round(statistics.mean(resultsd),3)              # setting rd to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    e = np.random.randint(200000, size=1000)         # array of size 1000
    start_time = time.time_ns()
    bucketSort(e)                                    # calling algorithm for array e
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultse = []
    resultse.append(time_elapsed)
re = round(statistics.mean(resultse),3)              # setting re to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    f = np.random.randint(200000, size=2500)         # array of size 2500
    start_time = time.time_ns()
    bucketSort(f)                                    # calling algorithm for array f
    end_time = time.time_ns()
    resultsf = []
    time_elapsed = (end_time - start_time)*10**-6
    resultsf.append(time_elapsed)
rf = round(statistics.mean(resultsf),3)              # setting rf to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    g = np.random.randint(200000, size=5000)         # array of size 5000
    start_time = time.time_ns()
    bucketSort(g)                                    # calling algorithm for array g
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsg = []
    resultsg.append(time_elapsed)
rg = round(statistics.mean(resultsg),3)              # setting rg to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    h = np.random.randint(200000, size=7500)         # array of size 7500
    start_time = time.time_ns()
    bucketSort(h)                                    # calling algorithm for array h
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsh = []
    resultsh.append(time_elapsed)
rh = round(statistics.mean(resultsh),3)              # setting rg to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    i = np.random.randint(200000, size=10000)        # array of size 10000
    start_time = time.time_ns()
    bucketSort(i)                                    # calling algorithm for array i
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsi = []
    resultsi.append(time_elapsed)
ri = round(statistics.mean(resultsi),3)              # setting ri to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    j = np.random.randint(200000, size=15000)        # array of size 15000
    start_time = time.time_ns()
    bucketSort(j)                                    # calling algorithm for array j
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsj = []
    resultsj.append(time_elapsed)
rj = round(statistics.mean(resultsj),3)              # setting rj to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    k = np.random.randint(200000, size=20000)        # array of size 20000
    start_time = time.time_ns()
    bucketSort(k)                                    # calling algorithm for array k
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsk = []
    resultsk.append(time_elapsed)
rk = round(statistics.mean(resultsk),3)              # setting rk to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    l = np.random.randint(200000, size=30000)        # array of size 30000
    start_time = time.time_ns()
    bucketSort(l)                                    # calling algorithm for array l
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsl = []
    resultsl.append(time_elapsed)
rl = round(statistics.mean(resultsl),3)              # setting rl to the mean of results rounded to 3 decimal places
for r in range(num_runs):
    np.random.seed(1)
    m = np.random.randint(200000, size=50000)        # array of size 50000
    start_time = time.time_ns()
    bucketSort(m)                                    # calling algorithm for array m
    end_time = time.time_ns()
    time_elapsed = (end_time - start_time)*10**-6
    resultsm = []
    resultsm.append(time_elapsed)
rm = round(statistics.mean(resultsm),3)              # setting rl to the mean of results rounded to 3 decimal places

bucketbench = [ra, rb, rc, rd, re, rf, rg, rh, ri, rj, rk, rl, rm] # setting bucketbench to an array of the results of timings for sorting arrays a-m