## Power - Mod Power

So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function as `a^b` shown below:

```
>>> pow(a,b) 
```
#### or

```
>>> a**b
```

<br>

It's also possible to calculate `a^b` mod `m`

```
>>> pow(a,b,m) 
```

This is very helpful in computations where you have to print the resultant `% mod`.

Note: Here, `a` and `b` can be floats or negatives, but, if a third argument is present, `b` cannot be negative.

Note: Python has a `math` module that has its own `pow()`. It takes two arguments and returns a float. Frankly speaking, we will never use `math.pow()`.

<br>

### Task:

You are given three integers: `a`, `b`, and `m`, respectively. Print two lines.

* The first line should print the result of `pow(a,b)`.
* The second line should print the result of `pow(a,b,m)`.

<br>

### Input Format:

The first line contains `a`, the second line contains `b`, and the third line contains `m`.

<br>

### Constraints :

```
1 <= a <= 10
1 <= b <= 10
2 <= m <= 1000
```

<br>

### Output format:

Print the result as described above.



### Example:

**Input:**

```
3
4
5
```
<br>

**Output:**

```
81
1
```
<br>

### Solution 

```python
a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))

print(pow(a,b,m))
```
<br>
