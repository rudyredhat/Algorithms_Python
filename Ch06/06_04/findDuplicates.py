import sys
import time


def findDuplicate3(arr):
    n = len(arr)
    # create an aux array with boolean as false
    aux = [bool]*n
    # iterate through the main array and lookup in the aux array
    for i in range(n):
        # take the ith ele
        tmp = arr[i]
        # now look up the ith ele in the aux array
        if aux[tmp] == True:
            # we got the duplicate and return it
            return tmp
        # otherwise update the aux array to True
        aux[tmp] = True
    return sys.minvalue



def findDuplicate2(arr):
    n = len(arr)
    # sort the list/array
    arr.sort()
    # no we need to start from next index , means from 1st index to nth index
    for i in range(1, n):
        # print(arr[i]," ",arr[i-1])
        if arr[i] == arr[i-1]:
            return arr[i]
    return sys.minvalue


def findDuplicate1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]
    # if we found no match, for this we used below and ret False
    return sys.minvalue


def testCase1(arr):
    n = len(arr)
    # iterate from 0 to n-1 value, so that (n) will contain the duplicate
    """
    for eg, n = 6 , 0,1,2,3,4,5
    so, for loop = 0 - range(5) = 0,1,2,3,4
    and then add the last ele, a[6-1]=a[5] = n-1=5
    so, 1,2,3,4,5,5
    """
    for i in range(n-1):
        arr[i] = i+1
    # last index we are filling that as duplicate
    arr[n-1] = n-1


def main():
    n = int(sys.argv[1])
    # we know worst case would be the ele present in the last
    # create a empty list of size n
    arr = [int] * n
    # so how to fill this array check the below function
    print(testCase1(arr))
    print(arr)
    start = time.time()
    # print(findDuplicate1(arr))
    # print(findDuplicate2(arr))
    print(findDuplicate3(arr))
    end = time.time()
    print("Time Taken: ", float(end-start))


if __name__ == '__main__':
    main()

