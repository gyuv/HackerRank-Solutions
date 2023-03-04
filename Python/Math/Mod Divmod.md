## Mod Divmod

One of the built-in functions of Python is `divmod()`, which takes two arguments `a` and `b` and returns a tuple containing the quotient of `a/b` first and then the remainder `a`.

For Example:

```
>>> print divmod(177,10)
(17, 7)

```
<br>

Here, the integer division is `177/10` which results in `17` and the modulo operator is `177%10` which results in `7`.

<br>

### Task:

Read in two integers, `a` and `b`, and print three lines.

* The first line is the integer division `a//b` (While using Python2 remember to import division from __future__).
* The second line is the result of the modulo operator: `a%b`.
* The third line prints the divmod of `a` and `b`.

<br>

### Input Format:

The first line contains the first integer, `a`, and the second line contains the second integer, `b`.

<br>

### Output format

Print the result as described above.

<br>

### Example:

**Input:**

```
177
10

```
<br>

**Output:**

```
17
7
(17, 7)

```
<br>

### Solution 

```python
a = int(input());
b = int(input());
print(a//b);
print(a%b);
print(divmod(a,b));
```
<br>

