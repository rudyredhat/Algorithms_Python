# Need of Algorithm Analysis
- **Problem:**` Given a sorted array, of n integers, Find an efficient algorithm that searches for ele x in the array.`
- **Soln:**
  - array is sorted and x is given, if x=1 ret True , if x=9 ret False
  `1 2 3 4 5`
- **Sol 1:** `Naive / Brute Force `
  - match (x) with each element one by one.
- **Sol 2:** `Divide & Prune Strategy`
  - go to random index and check whether (x) is smaller or greater than index
  - check the same thing with the left elements
- **Sol 3:** `Divide & Prune Strategy - 2`
  - go to middle index and search for the ele (x), if matched ret middle index
  - else we compare the ele is greater or smaller and skip the left over ele
- `How to use the better solution now ?`
  - take sol and convert it into lang and check for the time taken to execute and lesser the time 
  - this is quite lengthy process
  - so we need have a thinking process in mind to save all these efforts
