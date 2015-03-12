#Radix sort
def radixSort(A, base=10):
    maximum = 0

    for i in A:
        if abs(i) > maximum:
            maximum = abs(i)
    maxDigit = len(str(maximum))

    j = 1
    while j < maxDigit+1:
        buckets = [[]for i in range(base)]
        for i in A:
            buckets[(i%(base**j))/(base**(j-1))].append(i)

        A = []
        for k in buckets:
            A.extend(k)

        j+=1

    #bucket numbers by sign
    buckets = [[i for i in A if i<0],[i for i in A if i>=0]]
    A=buckets[0]+buckets[1]

    return A

if __name__ == '__main__':
    print radixSort([754,23,-1,44562,5,74556,-700099,-4,-6,-100,-201])