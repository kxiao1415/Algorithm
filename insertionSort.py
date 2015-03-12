import random

def insertionSort(array):
    for j in range(1, len(array)):
        i = j-1
        while i>-1 and array[i]>array[i+1]:
            key=array[i+1]
            array[i+1]=array[i]
            array[i]=key
            i=i-1
    return array

def generateRandomList(size=9):
    return [random.randint(-10,10) for i in range(size)]

if __name__ =='__main__':
    a=generateRandomList()
    print 'insertion sort:\n', a,'\n',insertionSort(a)


