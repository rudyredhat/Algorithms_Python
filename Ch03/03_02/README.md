#  Big O Notation
- When our function is behind some of the dominating function like n^2 and n^3 we have,
- consider the main `function <= c.n2`
- where `c = constant`
- but there are some point where our main function is dominating the `n^2`, 
  - `∃ no, ∃ c, where n >= no (n not)`
- so it means that when `n >= no` , the above main function will be true
```
     ∃no, ∃c
  2n^2+50n+100 ≤ c.n^2
               n ≥ no
```
- so to communicate the above function we write it as:
  - main function ≃ O(n2)
  - so it means => f(n) ≃ O(g)
- it means g is always having some multiplication (let's say c above) and there is two constants(∃ ) , so the function is always dominated by constant multiplied with g
- `f(n) <= c.g(n)`,   `∃ no, c` (if there exist two constants no and c here) are +ve int but for only if there is a cut point where ,` n >= no`
- looking at the egs below we always look for the `closet upper bond`
```
  1) n+50 ≈ O(n)
      n+50 ≤ c(n)
            n ≥ no
  2) n^2+100n+1000 ≈ O(n^2)
      n^2+100n+1000 ≤ c(n^2)
            n ≥ no
```
- consider the c=2 , so `function <= 2(n^2)` for some n>=no
