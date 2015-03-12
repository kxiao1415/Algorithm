#Three Sum algorithm
#find 3 numbers from the list that will sum up to a given number
#have a outer loop, looping the n-2 times from the sorted array, 2 indecies pointing to both sides for matching up
#complexity is O(n^2)

def ThreeSum(array, number):
    a = array[:]
    a.sort()

    solution = []
    for i in range (len(a) - 2):
        j = i + 1
        k = len(a) - 1

        while (j < k):
            s = a[i] + a[j] + a[k]
            if s == number:
                solution.append([a[i], a[j], a[k]])
                j += 1
                k -= 1
            elif s < number:
                j += 1
            else:
                k -= 1
    return solution

print ThreeSum([6,4,3,2,7,8,5,1], 10)
