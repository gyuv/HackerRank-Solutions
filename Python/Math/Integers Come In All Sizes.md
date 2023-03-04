## Integers Come In All Sizes

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: `2^31 - 1 (c++ int)` or `2^63 - 1` (C++ long long int).
As we know, the result of `a^b` grows really fast with increasing `b`.
Let's do some calculations on very large integers.

<br>

### Task:

Read four numbers, `a`, `b`, `c`, and `d`, and print the result of a <sup> b </sup> + c <sup> d </sup>

<br>

### Input Format:

Integers `a`, `b`, `c`, and `d` are given on four separate lines, respectively.

<br>

### Constraints:

```
1 <= a <= 1000
1 <= b <= 1000
1 <= c <= 1000
1 <= d <= 1000
```

<br>

### Output format:

Print the result of a<sup>b</sup> + c<sup>d</sup> on one line.

<br>

### Example:

**Input:**

```
9
29
7
27
```
<br>

**Output:**

```
4710194409608608369201743232
```
Note: 
<br>
This result is bigger than 2<sup>63</sup> - 1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.

<br>

### Solution 

```python
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print((A**B)+(C**D))
```
<br>
