# Omega, Theta, Small o Notation  

## Aymptotic Approach - Lower Bond - Ω (Omega) - Time & Space
- For the function that is being written up we have used , Big Oh (O) for the upper bound.
- Now for the lower bond we are using Omega (Ω) .
- So for the function = `2n^2+50n+100 >= c.n^2` so there exists some `∃no (n not), ∃c`, but the function is not greater than for every n.
- For some point of n only the above function is satisfied, i.e `n >= no`
```           
1)
     ∃no, ∃c
  2n^2+50n+100 ≥ c.n^2
               n ≥ no
2) 2n^2+50n+100 ≈ Ω(n^2)

3) f(n) is Ω(g(n)) only if exist two contants here, ∃no,c > 0
   s.t f(n) ≥ Ω(g(n)) for n ≥ no , this has to be satisfied
```
- so it means our function is always above the curve when constant shrink is available.
- for eg `2n^3+50n+100 ≈ Ω(n^3)` , so we take the highest power degree.
- but the function will also satify for `Ω(n)`, but we need to check for the lowest nearest bond function.
- so we choose the highest power degree which is `Ω(n^3)`.

## Aymptotic Approach - Middle Bond - θ (Theta) - Time & Space
- So after some value of n, the function will be dominated by some value and some value will be lesser than the function.
- Our f(n) will be in the middle of the both the upper and the lower bond functions.
```           
1) 2n^2+50n+100 ≈ θ(n^2)

2) f(n) is θ(g(n)) only if,
   s.t f(n) ≈ O(g(n)) , f(n) has upper bond of g(n)
   s.t f(n) ≈ Ω(g(n)) , f(n) has lower bond of g(n)
```
- eg, `5n^2 + 100 ≈ θ(n^2)` satisfies both the upper and lower bond.

## Aymptotic Approach - o (Small o) - Time & Space
```           
1) f(n) is o(g(n)) iff, ∃no,c > 0
   s.t f(n)< c.(g(n)) ∀ n ≥ no 
```
- here the function never touches the g(n), its always less than the g(n).
