# Compress the String!

### Task
In this task, we would like for you to appreciate the usefulness of the `groupby()` function of `itertools`. You are given a string. Suppose a character `c` occurs consecutively n times in the string. Replace these consecutive occurrences of the character `c` with `(n, c)` in the string.

For a better understanding of the problem, check the explanation.

<br>


### Input Format
A single line of input consisting of the string.

<br>


### Output Format
A single line of output consisting of the modified string.

<br>

### Constraints
All the characters of the string `S` denote integers between 0 and 9.

<br>


### Sample Input
```
1222311
```

<br>

### Sample Output
```
(1, 1) (3, 2) (1, 3) (2, 1)
```

<br>

### Explanation
First, the character `1` occurs only once. It is replaced by `(1, 1)`. Then the character `2` occurs three times, and it is replaced by `(3, 2)` and so on.

Also, note the single space within each compression and between the compressions.

<br>

## Solution
```python
from itertools import groupby

s = input()

for k, g in groupby(s):
    print((len(list(g)), int(k)), end=' ')
```
