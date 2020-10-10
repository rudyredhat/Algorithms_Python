# Need of Asymptotic Analysis
- analyse algo for time consuming
- complex function needs to analyze in a better way
```           
                Time              Space
1) Algorithm 1: 2n^2+50n+100      n+50
                ops               units
2) Algorithm 2: 3n^3+5n^2+5n+100  n^2+n+50
                ops               units
```
- **Approach 1** to simply take the dominating one - `cancellation approach`
```           
                Time              Space
1) Algorithm 1: 2n^2+50n+100      n+50
                ops               units
2) Algorithm 2: 3n^3+5n^2+5n+100  n^2+n+50
                ops               units
```
- **Approach 2** - `asymptotic approach`
	- when n is approaching infinity, consider a new function similar to above one which will give the equivalence of the behaviour for large value of n        
  `Asymptotic approach  -----> n -> ∞`
