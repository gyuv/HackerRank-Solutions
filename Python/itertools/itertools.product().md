## itertools.product()

<br>

[itertools.product()](https://docs.python.org/2/library/itertools.html#itertools.product)
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, `product(A, B)` returns the same as `((x,y) for x in A for y in B)`.

#### Sample Code:
```python
from itertools import product

print(list(product([1,2,3],repeat = 2)))
# Output: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print(list(product([1,2,3],[3,4])))
# Output: [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]

A = [[1,2,3],[3,4,5]]
print(list(product(*A)))
# Output: [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))
# Output: [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```
<br>

#### Task:

You are given two lists `A` and `B`. Your task is to compute their cartesian product `A x B`.

#### Example:
```python
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```
Note: `A` and `B` are sorted lists, and the cartesian product's tuples should be output in sorted order.

#### Input Format

* The first line contains the space separated elements of list `A`.
* The second line contains the space separated elements of list `B`.

Both lists have no duplicate integer elements.
<br>

#### Constraints
```
$0 < A < 30$
$0 < B < 30$
```
<br>

#### Output Format

Output the space separated tuples of the cartesian product.
<br>

#### Sample Input
```
1 2
3 4
```
<br>

#### Sample Output
```
(1, 3) (1, 4) (2, 3) (2, 4)
```
<br>

## Solution in Python 3
```python
from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ");
```
<br>

## Solution in Python 2
```python
from itertools import product

A = raw_input().split()
A = list(map(int, A))
B = raw_input().split()
B = list(map(int, B))

for i in product(A, B):
    print i,
```






