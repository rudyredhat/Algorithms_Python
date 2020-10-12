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

- `Soln3: DS Pattern: Array Lookup `
  - for the single size array, we can have a hint present in the problem 
  - take one extra `auxilary` array of same size
  - initially set all the value of `aux` array to false
  - now iterate through the main array one by one and set the values to true
  - at the third iteration we have found `2` once again, so we can mark it as duplicate rather than scanning the full array
  ```
  n = 5
  4 3 2 1 2
  0 1 2 3 4
  
  f f f f f --- 1st
  0 1 2 3 4
  
  f f t t t --- 2nd
  0 1 2 3 4
  
  f f t t t --- 3rd
  0 1 2 3 4
  ```
  - so here we are using a extra space and can be called as a `data structure` , we will look into later.
  - 1 iteration, 1 comparison and 1 update and all we can call this as low level operation 
  - just if the ele is at last , we can have this `n` operation as twice
  - for space we just need extra space of n units
  - T.C = 2*n = θ(n)
  - S.C = θ(n)
