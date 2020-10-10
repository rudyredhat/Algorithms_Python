# Find missing number , Coding interview problem

- **Problem** - `Given an array of n integers , consisting of 1 to n+1 without repetition, find an efficient algo , that returns the missing number.`
- **Solution:** 
- Always take a bunch of soln and follow 4 phase: `(Problem, Thinking Process, Analysis, Coding)`
- Case :
- n = 5
- arr index range => n = 0 to n = 4 
```
      0 1 2 3 4
      6 1 5 4 3
```
- so here the missing number is 2 and we need to generate the algo 
- **Solution 1 / Algorithm 1:** 
	- checking all the numbers less than (n) , one-by-one
	- first check (1) in the given array and one-by-one find the missing one
	- so we need to give a name `(Adhoc)` and under than we have `(Naive)` strategy
- We need to check for 2 metrics `(Time)` processor & `(Space)` ram for all the algo
- We need to perform the analysis part from the Time and Space Complexity
- **Solution 2 / Algorithm 2:**
```
      0 1 2 3 4
      6 1 5 4 3
```
- We can sort the above array and check the missing number
```
      0 1 2 3 4
      1 3 4 5 6
```
- But here a work called `sort` is being performed
- so this is again `(Adhoc)` strategy but the thinking part is `(Sort + Scan)`
- so we can check 2 metrics here for all the analysis before code
- **Solution 3 / Algorithm 3:**
```
      0 1 2 3 4
      6 1 5 4 3
```
- take another empty array with n+1 arr index range
```
      0 1 2 3 4 5 6
      θ θ O θ θ θ θ
```
- so we can see extra memory space (2) is being used, and we are cutting down (θ) all the ele that are being found
- so this type of thing we are using as collection , which is termed as `(data structure)` pattern in which sub-context we have `(1-d array)`
