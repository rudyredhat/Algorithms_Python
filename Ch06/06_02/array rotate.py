#!/usr/bin/python
import sys
import time


# T.C = θ(kn) , S.C = O(1)
def rotatearr1(arr, k):
    n = len(arr)
    # iterating through k times , the whole shift operation below
    for i in range(k):
        # take the last ele
        last = arr[n-1]
        # iterate the loop from 2nd last ele to -1 from backwards
        # always have some eg value, like n=10 to get better picture
        for j in range(n-2, -1, -1):
            arr[j+1] = arr[j]
        # now copy the 0th index to last
        arr[0] = last


# T.C = θ(n) , S.C = θ(n)
def rotatearr2(arr, k):
    n = len(arr)
    # here we need to have an aux array
    aux = [0]*n
    # we are going through each element to map to aux array
    for i in range(n):
        # so we are mapping i+k value to the desired place
        # sometimes (i+k) can go outside the boundary , so we need to have mod of size
        aux[(i+k)%n] = arr[i]
    # we need to copy this aux array back to the input array
    for i in range(n):
        arr[i] = aux[i]




def main():
    # take the values from calling of program
    # pycharm - run - edit configuration - set parameter - apply - ok
    n = int(sys.argv[1])
    # 10 blank index values
    arr = [0]*n
    # fill the arr value
    for i in range(n):
        arr[i] = i+1
    # int value calculate for the number of values to shift for diff k values
    # k = n//2
    k = n-1
    # to test large values comment the below print
    # print(arr)
    print(k)
    start = time.time()
    rotatearr2(arr, k)
    end = time.time()
    print("Time taken:", (end-start), "seconds")
    # print(arr)


if __name__ == '__main__':
    main()