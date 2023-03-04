# itertools.combinations_with_replacement()
[itertools.combinations_with_replacement(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement)
<br>
This tool returns `r` length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
<br>

#### Sample Code
```
>>> from itertools import combinations_with_replacement
>>> 
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
```
<br>

#### Task
* You are given a string `s`.
* Your task is to print all possible size `k` replacement combinations of the string in lexicographic sorted order.
<br>

#### Input Format
 A single line containing the string `S` and integer value `k` separated by a space.
<br>

#### Constraints
 `0 < k <= len(S)`
 The string contains only UPPERCASE characters.
 <br>

#### Output Format
Print the combinations with their replacements of string `S` on separate lines.

#### Sample Input
```
HACK 2
```
<br>

#### Sample Output
```
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
```
<br>

### Solution
```python
from itertools import combinations_with_replacement

s, k = input().split()

for combination in combinations_with_replacement(sorted(s), int(k)):
    print("".join(combination))
```
<br>

### Explanation
* We start by importing the `combinations_with_replacement` function from the `itertools` module.
* We read the input string `s` and integer `k` from the user, and split them using the `split()` method to obtain separate values for `s` and `k`.
* We use the `sorted()` function to sort the characters in the string `s`.
* We then use a `for` loop to iterate through all the combinations with replacement of length `k` of the sorted string `s` using the `combinations_with_replacement()` function.
For each combination, we use the `join()` method to concatenate the characters in the combination into a string and print it to the console.
<br>

Note: It is important to convert the integer value of `k` to an integer using int() before passing it to the `combinations_with_replacement()` function.
