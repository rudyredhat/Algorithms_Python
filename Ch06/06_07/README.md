# Merge Sorted Arrays
- **Prob:**`Given two sorted array integer arrays n1 and n2, merge n2 into n1 as one sorted array`
- **Soln:**`
  ```
    n1 = [1,2,3,0,0,0] , m=3
    n2 = [2,5,6] , n=3
    o/p = [1,2,3,4,5,6]
    - we have extra spaces in n1, so that total size of n1 = m+n
  ```
  - so check for the smallest one from both the array
  - we have the first number exactly the smallest from both n1 and n2
  - compare `0: n1` and `0: n2' and add in the output array
  - then move forward from the index which `index` value we have output in the final array
  - compare the next index values from the array and so on
  - but we do not want the `extra` array, so we can have `another techq`
  - we can move from `backwards` and compare the `ele` from backwards, the largest of `two` ele
  - check the last two values and which is `largest` just copy that ele to the `last` of the `n1` and move on adding ele from last
  ```
    n1 = [1,2,3,0,0,0] , m=3
    n2 = [2,5,6] , n=3
    6 => 3
    n1 = [1,2,3,0,0,6]
    n2 = [2,5]
    5 => 3
    n1 = [1,2,3,0,3,6]
    n2 = [2]
    3 => 2
    n1 = [1,2,3,3,3,6]
    2 => 2
    n1 = [1,2,2,3,3,6]
  ```
  T.C = θ(n+m)
  S.C = O(1)
