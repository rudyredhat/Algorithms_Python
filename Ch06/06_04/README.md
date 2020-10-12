# Find Duplicates in an Array -PART 1 || Coding Interview Problem  
- **Prob:**`Given an array consisting of n integers in which each element is between 1 to n-1. Find an efficient algorithm that return any duplicate integer exists in the array`.
```
  n = 5
  4 3 2 1 2
  0 1 2 3 4
  
  o/p: 2
  
  n = 6
  5 4 2 5 3 2
  0 1 2 3 4 5 
  o/p: 2 or 5 (return anyone)
```
- **Soln:**
- `Soln1: Naive/Brute Force`
  - take the `first ele` and match that ele to all the rest ele , then the `next ele`
  ```
  n = 5
  4 3 2 1 2
  0 1 2 3 4
  
  4-3, 4-2, 4-1, 4-2
  3-2, 3-1, 3-2
  ```
  - so we can have the worst case scenario, when the duplicate ele is present at the last.
  - time is always the low level operations that we have so we are having n-1, n-2 .. so on comparisons till end.
  - for space we have some constant var which can be used for the iterations.
  - T.C = (n-1)+(n-2)+(n-3)+....+1 = (n-1)n/2 = θ(n^2)
  - S.C = O(1)

- `Soln2: Adhoc: Sort+Scan`
  - sort the input array first and search the ele one by one after another
  ```
  n = 5
  4 3 2 1 2
  0 1 2 3 4
  
  1 2 2 3 4
  1-2, 2-2 -- we found a match here, stop
  ```
  - So sorting algo takes `nlogn` which we will see later and except for last ele we are not comapring it
  - In the same array we are having the sorting done, along with some extra var
  - T.C = nlon + (n-1) = θ(nlogn)
  - S.C = O(1)
