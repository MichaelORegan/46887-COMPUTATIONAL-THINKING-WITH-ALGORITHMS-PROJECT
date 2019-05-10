# Michael O'Regan 05/May/2019
# https://www.sanfoundry.com/python-program-implement-bucket-sort/

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
 
alist = [54,26,93,17,77,31,44,55,20]
bucketSort(alist)
print(bucketSort(alist))