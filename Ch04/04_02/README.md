# Worst, Best, Average Case Analysis  
- Life of Algorithm depends on the input given to the algorithm, just same as Life of human being.
```
    Life of Algorithm = for both Time & Space can be analyse
    |                   & we get bunch of functions, we have symbols to simplify them = O, Ω, θ, o
    |
    |_ Best Case
    |_ Worst Case
    |_ Average Case
    |_ Amortized Analysis (will discuss later)
```
- So some consider that O is best case, θ  worst case & Ω is avg case. --> `this is completely meaningless understanding.`
- Best Case cannot be used for the indicator of the algorithm, because we cannot predict the future.
- Worst Case can be predicted with the whole set of life time. `Gauranteed Performance` , e.g Covid.
- Avg Case: Estimate diff set of inputs, not with 2-3 inputs even if it coming as worst case. `Practicle Performance`.g T20.
- Always we must focus on the Worst Case for the algorithms

## Problem statemnet to discuss the life of algorithm.
- **Prob:** `Perform the Search Statement from the array.`
- **Soln:**
  ```
    x = 5
    10 20 50 5 8 6
  ```
  - `Linear Search:` We can search one by one and find out the element.
  ```
  Linear_Search(ar, x)
    for(i=0; i<n; i++)
      {if(ar[i] == x)
      return True
      }
      return False
  ```
  - Now we compute the Analysis
  ```
  Best Case Analysis:
  - If we found the ele at the first point of time, we get the best case for time.
  - So here we are doing 1 comparison = which is combined to as = c = constant
  - Time = c operations ≈ O(1) 
  - Now we apply any symbol to the c , which we have given above
  - 1 meaning here is ≤ c(1)
  - Space: c units  ≈ O(1) 
  - 1 var we are using here.
  ```
  ```
  Worst Case Analysis:
  - so we have given the x , and we are keep on comparing and x is not there, and ret false
  - we never focus on the low level operations, we are focusing on the core of the algorithm.
  - Time = c*n operations ≈ θ (n) 
  - so θ (n), is just like the middle bond where we can not have O(n) and Ω(n).
  - Space: c units  ≈ O(1) 
  ```
  ```
  Average Case Analysis:
  - Keep on giving up diff x values for diff locations.
  - If for some algo worst case is very bad we need to go for avg case, otherwise always need to 
    consider worst case.
  - Time = 1+2+3+4+...+n    n(n+1)    (n+1)
           ______________ = ______ = _______ = θ (n)
                  n           2*n       2
  - for every positions we need to increment the comparisons 
  - and we are we using n comparisons , so we are dividing by n.
  - Space: c units  ≈ O(1) 
  ```
 **`So its upto you , as per any algorithm for calculating Time & Space Complexity , we can assign any symbol.`**
