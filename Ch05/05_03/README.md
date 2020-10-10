# Truth Behind Zero Indexing  
- Lets consider an array:
```
      1000   1004  1008  1012  1016      -- starting add of each ele (size of ele = 4 bytes)
 a =    50    40    30    40    70
 C 1 =  0     1     2     3     4        -- 0 base indexing sys
 C 2 =  1     2     3     4     5        -- 1 base indexing sys
```
- so to access any ele compiler use `a[i] = a(starting addr) + i(ith index) * (size of ele)` for `0 base indexing sys`
- C 1 : a[1] = 1000 + (1*4) = 1004
- **Benefit:** `We are saving one subtraction in 0 base indexing format`.

- so to have access as C 2 `a[i] = a(starting addr) + (i-1) * (size of ele)` for `1 base indexing sys`
- C 2 : a[1] = 1000 + ((1-1)*4) = 1000
