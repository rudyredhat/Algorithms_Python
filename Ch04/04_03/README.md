# Overview of Storage Patterns
- repetition , i.e why called patterns
- 2 groups
- **Linear Storage Pattern**
	- `Sequential`
		- Ele are stored at contiguous locations in RAM
		- access become fast
		- contiguous location will create a storage concern
	- `Linear Linked`
		- Each address (a1, a2 .. an) is connected to (e1..en)
```
e1 a1
 🗲
e2 a2
  🗲
e2 a3
```
- **Non-Linear Storage Pattern**
	- `Tree Storage`
		- root at the top and branches at the end
		- we can not get a linear movement of all data
	- `Hash Storage`
		- have bunch of buckets, and when ele comes up
		- it goes and match with the hash function
		- so total we have k buckets and do some function
		- and the key is mapped to one bucket 
		- and what kind of buckets should look like ?
		- depends on the type / storage and in most storage 
				have linked storage
