# Find all anagram present in the string
- **Prob:**`All anagram in a string`
- **Soln:**`
  ```
    s1 = c b a e b a b a c d
    s2 = a b c
  ```
  - sort s2 first and count the length`(n)`  of s2
  - take the first `(n)` element from s1, and check if matches with s2
  - then again move the index to 1, perform the above step

