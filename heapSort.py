#heap data structure, priority queue, heapsort algorithm
def maxHeapify(A, i):
    heapSize = len(A)
    l = i*2+1
    r = i*2+2
    greatest=i
    
    if l<=heapSize-1 and A[l]>=A[i]:
        greatest=l
    if r <= heapSize-1 and A[r]>=A[greatest]:
        greatest=r
    if i != greatest:
        temp=A[i]
        A[i]=A[greatest]
        A[greatest]=temp
        maxHeapify(A, greatest)
        
    return A

        
def buildMaxHeap(A):
    heapSize = len(A)
    i = heapSize/2
    
    while i >= 0:
        maxHeapify(A, i)
        i-=1
        
    return A


def heapSort(A):
    A=buildMaxHeap(A)
    i = 0
    while i < len(A):
        A=A[:i]+buildMaxHeap(A[i:])
        i+=1
        
    return A

if __name__=='__main__':
    A=[4,5,2,1,6,8,9,3,7]

    print heapSort(A)


