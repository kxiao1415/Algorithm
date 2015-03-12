from insertionSort import generateRandomList

def maxSubArray(array):
    maxEndHere = maxSoFar = array[0]
    for i in array[1:]:
        maxEndHere=max(i,maxEndHere+i)
        maxSoFar =max(maxEndHere,maxSoFar)
    return maxSoFar

if __name__=='__main__':
    a=generateRandomList()
    print 'max sub array of: \n%s \nis %s'%(a,maxSubArray(a))
