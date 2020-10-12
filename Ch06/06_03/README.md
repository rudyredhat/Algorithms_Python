# Anagram Check || Coding Interview Problem  
- **Prob:**`Given two strings, S1 & S2 , find an efficient algorithm to determine whether S1 & S2 are anagram of each other or not ?`
```
 Anagram: Is permutation of S1 is S2 or permutation of S2 is S1 ?
  e.g 1
      S1 = a b a a c
      S2 = a c a b a
      o/p: True
  e.g 2
      S1 = a b a c
      S2 = c a b b 
      o/p: False
```
- **Soln:**
- `Soln 1: Naive / BruteForce`
  - This is what we can have most simplest strategy by having very raw form of thinking.
  ```
      S1 = a b a a c
      - Search for each ele ony by one and replace it with some special marker.
      - Either we can cross the ele one by one out from S2
      S2 = a c a b a
      o/p: True
  ```
  - T.C = n + (n-1) + (n-2) + ......+ 1
        = n(n+1) / 2 = θ(n^2)
  - S.C = O(1) 
  - Just we need to scan this up, with few var we can have the output.
  - So n^2 algo is painful , as n increase it will take more time.
  
- `Soln 2: Adhoc Thinking (Sort+Scan)`
  - Only specific to this kind of problems.
  - Going through each ele one by one , its better to sort bot the S1 & S2.
  - And then we can check the ele one by one linear, rather than going through the whole S2.
  ```
      S1 = a b a a c
      S2 = a c a b a
  Sort S1 = a a a b c
  Sort S2 = a a a b c
      o/p: True
  ```
  - T.C = nlogn + nlogn + n = θ(nlogn) `later we will check for sorting why nlon?`
  - S.C = O(1)
- `Soln 3: Adhoc Thinking`
  - To void sorting we will use diff techq
  - We can have the frequencies of all the char of S1 in a separate box and later can match with the freq of S2
  - So with some extra space we can have better time value.
  - Suppose if we only have small letter , so we can take extra memory of 26
  - So how to map a,b,c to the box of array with 0,1,2?
    - We can have a function where the values of the character are `S1` which can be calculated by always subtracting with `a`.
    - eg = character - 'a' = 97-97 = 0 (0 index of the array) , a-a, b-a, a-a, a-a, c-a
  - Now go to the `S2` after we have the Box with the counter now check the values from `S2` one by one.
  - If the values is there `decrement` the counter from the Box.
  ```
      S1 = a b a a c

      B  = 3 1 1 0 0 . . . . 0
           0 1 2 3 4 . . . . 25
           
      S2 = a c a b a

      B  = 0 0 0 0 0 . . . . 0
           0 1 2 3 4 . . . . 25

      - so if all the Box value is 0, the S1 = S2
      o/p: True
  ```
  - we are just doing `n` iterations for both increment and decrement.
  - As the string size can be 1 billion but the box size is always fixed as 26.
  - T.C = (n + n)*c = θ(n)
  - S.C = O(1)
