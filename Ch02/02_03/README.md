# Understanding Log N
- Case 1: **Repeated Doubling**
	- 1 rabbit gives = 2 birth = 2^1
	- 2 rabbit gives = 4 birth = 2^2
	- n rabbit gives = n ??? = 2^d at dth day
	- 2^d = n
	- `d = log n (base 2)`
	- ? = log 1024 (base 2) ---> d = 10
	- ? = log 10^6 (base 2) = log 2^20 (base 2) ---> d = 20
- Case 2: **Repeated Half**
	- think of covid scenario
	- n day ------ = n persons
	- n/2^1 day ---- = n/2 
	- n/2^2 day ---- = n/4
	- n/2^d day - 1 ???? how many days to reach 1 person
	- n/2^d = 1
	- n = 2^d
	- `d = log n (base 2)`
- Case 3: **Spread Measure**
	- spread of covid
	- 0 day  - 1 people = 2^1 - 1
	- 1 day -- 2 people = total = 1+2 = 3 people = 2^2 -1
	- 2 day ---- 4 people = total = 4+3 = 7 people = 2^3 - 1
	- after how many days will we have (n) cases ? = 2^d+1 - 1
	- 2^(d+1) - 1 = n
	- 2^(d+1) = n +1
	- d+1 = log (n+1) (base 2) ----> `d = log (n+1) (base 2) -1`