import sys
import time


def findDuplicate(arr):
    n = len(arr)
    for i in range(n):
        # no we need to start from next index
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]
    # if we found no where a match, for this we used below and ret False
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
    print(findDuplicate(arr))
    end = time.time()
    print("Time Taken: ", end-start)


if __name__ == '__main__':
    main()

