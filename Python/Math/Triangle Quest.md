# Triangle Quest

You are given a positive integer `N`. Print a numerical triangle of height `N – 1` like the one below:
```
1
22
333
4444
55555
```
Can you do it using only arithmetic operations, a single for loop, and a print statement? Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
<br>

#### Note: Using anything related to strings will give a score of `0`.
<br>

#### Input Format
A single line containing an integer, `N`.
<br>

#### Constraints
```
1 <= N <= 9
```
<br>

#### Output Format
Print N – 1 line as explained above.
<br>

#### Sample Input:
```
5

```
<br>

#### Sample Output:
```
1
22
333
4444
```
<br>

## Solution  1:

```python
for i in range(1,int(input())):
    print(i*((10**i-1)//9))
```
<br>

## Solution  2:

```python
for i in range(1,int(input())):
    print (i * int(bin(2**i - 1)[2:]))
```

