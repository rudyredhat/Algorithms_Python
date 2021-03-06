# Rotate Array by K Elements || Coding Interview Problem  
- **Prob:** `Find an efficient algorithm to rotate an array by k positions to the right.`
```
    i/p:
    2 5 8 4 1 3 5
    0 1 2 3 4 5 6
    
    so if k = 3
    
    o/p:
    1 3 5 2 5 8 4
    0 1 2 3 4 5 6
    
```
- **Soln:**
- `Soln 1`
  - Simplest `Naive` strategy can be shift ele ony by one to get the kth ele.
  ```
      2 5 8 4 1 3 5
      5 2 5 8 4 1 3   - 1
      3 5 2 5 8 4 1   - 2
      1 3 5 2 5 8 4   - 3
  ```
  - so everytime there is `n` operations and with few const var we can shift the values.
  - T.C = θ(kn)
  - S.C = O(1)
- `Soln 2`
    - `Adhoc Strategy:` any relation we can have we can ouput the ele to the exact index using circular tecq.
    - so we are taking a `temporary array` or `auxilary array` , adding up the `(index + k)`
    - but how to get the index of the element after `k`?
    - so `(4+3) = 7`, we are taking `mod` where `7-7 = 0`, so shift the ele to 0.
    - similarly `(5+3) = 8`, `8-7 = 1`
    ```
      2 5 8 4 1 3 5
      0 1 2 3 4 5 6
      
            2 5 8 4
      0 1 2 3 4 5 6  -- aux array
      
      1 3 5 2 5 8 4
      0 1 2 3 4 5 6  -- aux array
    ```
    - so in 1 scan of the array we get the answer, but we need an `extra` array otherwise we can loose an ele.
    - T.C = θ(n)
    - S.C = θ(n)
- `Soln 3`
    - But the thing is that we are using an `auxilary array` and when we are increasing the arrat size say 1 billion, it will become bigger and bigger.
    - Any way we can `swap` the corresponding values, we can have our result.
    ```
        2 5 8 4 1 3 5
        5 3 1 4 8 5 2   -- but the result is not in correct order
        1 3 5 2 5 8 4   -- reverse/swap the half-half (k & independent) part (531) & (4852)
    ```
    - T.C = `n/2` op(1st stage) + `k/2` op(for k ele) + `(n-k)/2` op(for independent ele) = θ(n)
    - S.C = O(1)
