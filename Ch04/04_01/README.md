# Simple Summations  
1) Consider the summation: `1+2+3+4+5+......+n`
 - writing the above in reverse direction and add both of them
 ```
  1+2+3+4+5+......+n            = n*(n+1) / 2
  n+(n-1)+(n-2)+(n-3)+......+1
  -------------------------------
  (n+1)+(n+1)+(n+1)+.......(n+1)
  ```
 - but we need the first part only, so we are dividing by 2
 - so in the above arithmetic we have the diff is 1, so we can use this kind of techq called `Arithmetic Series Sum`.

2) Consider the summation: `1+r+r^2+r^3+......+r^(n-1)`
 - so we can check the diff between them is `r`. So this kind of sum is called `Geometric Series Sum`
 ```
 1+r+r^2+r^3+......+r^(n-1)       = s
 r+r^2+r^3+......+r^(n)           = s * r
 -----------------------------------
 1+(cancel all the terms) + r^(n) = (s*r - s) = (r^(n) - 1)
 ------------------------------------
 (s*r - s) = (r^(n) - 1)
 s(r-1) = (r^(n) - 1)
 s = (r^(n) - 1) / (r-1)
 ```
