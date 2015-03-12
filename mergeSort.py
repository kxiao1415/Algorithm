from insertionSort import generateRandomList
 
def mergeSort(array):
   
    if len(array)>1:
        mid = len(array)//2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i,j,k=0,0,0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                array[k]=leftHalf[i]
                i+=1
            else:
                array[k]=rightHalf[j]
                j+=1
            k+=1
           
        while i<len(leftHalf):
            array[k]=leftHalf[i]
            i+=1
            k+=1

        while j<len(rightHalf):
            array[k]=rightHalf[j]
            j+=1
            k+=1
   
    return array

if __name__=='__main__':
    a=generateRandomList()
    print 'merge sort:\n', a,'\n',mergeSort(a)
