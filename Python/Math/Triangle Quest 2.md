## Problem Statement

You are given a positive integer `N`. Your task is to print a palindromic triangle of size `N`.

For example, a palindromic triangle of size `5` is:

```
1
121
12321
1234321
123454321
```

You can’t take more than two lines. The first line (a for-statement) is already written for you. You have to complete the code using exactly one print statement.

<br>

### Input Format:

A single line of input containing the integer `N`.

<br>

### Constraints:

* 0 < N < 10

<br>

### Output format

Print the palindromic triangle of size `N` as explained above.

<br>

### Example:

**Input:**

```
5
```

**Output:**

```
1
121
12321
1234321
123454321
```
<br>

### Solution 1

```python
for i in range(1, int(input()) + 1): 
    print((10 ** i - 1) ** 2 // 81)
```
<br>

### Solution 2

```python
for i in range(1,int(input())+1): 
    print (((10**i - 1)//9)**2)
```
<br>






