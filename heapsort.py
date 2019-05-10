# Michael O'Regan 06/May/2019
# https://www.programiz.com/dsa/heap-sort

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
 

alist = [54,26,93,17,77,31,44,55,20]
heapSort(alist)
print(alist)