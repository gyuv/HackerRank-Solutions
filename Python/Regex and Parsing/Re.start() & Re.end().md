# Re.start() & Re.end()


## Problem Description
You are given a string `s` and a substring `sub`. Your task is to find the indices of the start and end of sub in `s`.

## Input Format
The first line contains the string `s`.
The second line contains the string `sub`.

## Constraints
```
1 <= len(s) <= 100
1 <= len(sub) <= len(s)
```
## Output Format
Print the tuple in this format: (start_index, end_index).
If no match is found, print (-1, -1).

### Sample Input
```
aaadaa
aa
```

### Sample Output
```
(0, 1)  
(1, 2)
(4, 5)
```
## Explanation
The substring aa appears in the following positions in `aaadaa`:

* Starting at index `0` and ending at index `1`.
* Starting at index `1` and ending at index `2`.
* Starting at index `4` and ending at index `5`.
Hence, the output is `(0, 1), (1, 2), and (4, 5)`.

## Solution 1:
```python
s = input().strip()
sub = input().strip()

matches = [(start, start+len(sub)-1) for start in range(len(s)) if s.startswith(sub, start)]
if matches:
    for match in matches:
        print(match)
else:
    print((-1, -1))
```

## Solution 2:
```python
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)
```
