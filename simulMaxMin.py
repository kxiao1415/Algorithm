#simultaneous maximum and minimum

def simulMaxMin(lst):

    if len(lst)%2 == 0:
        currentMaximum = max(lst[:2])
        currentMinimum = min(lst[:2])

        irange = range(2,len(lst),2)
        
    else:
        currentMaximum = lst[0]
        currentMinimum = lst[0]

        irange = range(1,len(lst),2)

    for i in irange:
        
        currentMaximum = max(currentMaximum, max(lst[i:i+2]))
        currentMinimum = min(currentMinimum, min(lst[i:i+2]))

    return [currentMaximum, currentMinimum]


if __name__=='__main__':

    print simulMaxMin([1,-100,2,3,5,6,4,4,6,7,10,-1,5,100,-3,99,-20])
