#returns the count of 1's in a binary number

def numOnes(num):
    count = 0
    while (num != 0):
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count

print numOnes(7)
