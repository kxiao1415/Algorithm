#insertionSort given first and last positions
def insertionSort(array,l,r):
    for j in range(l+1,r+1):
        i = j-1
        while i>l-1 and array[i]>array[i+1]:
            key=array[i+1]
            array[i+1]=array[i]
            array[i]=key
            i=i-1
    return array

#Quick sort with median of three as pivot
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

    return A

def medianOfThree(A, l, r):
    mid = (l+r)/2
    
    if A[l]>A[r]:
        swap(A,l,r)
    if A[mid]<A[l]:
        swap(A,l,r)
    elif A[mid]<A[r]:
        swap(A,mid,r)

    return A[r]

def partition(A, l, r):
    pivot = medianOfThree(A,l,r)
    
    i=l
    j=l
    while j < r:
        if A[j]<pivot:
            swap(A,i,j)
            i+=1
        j+=1
    swap(A,i,r)

    return i

#need to random shuffle the Array to guarantee against the worst case (quadraic)
def quickSort(A,l,r):
   if r-l<3:
      insertionSort(A,l,r)
   else:
      p=partition(A,l,r)
      quickSort(A,l,p)
      quickSort(A,p+1,r)
   
   return A

#print quickSort([5,2,4,4,1,3,6,7,8,-1,89,-79],0,11)
