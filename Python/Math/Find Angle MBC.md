## Problem Statement

`ABC` is a right triangle, `90°` at `B`. Therefore, angle `ABC = 90°`. Point` M `is the midpoint of hypotenuse `AC`. 
You are given the lengths `AB` and `BC`. Your task is to find the angle `MBC` in degrees.
<br>
### Input format:

The first line contains the length of side AB. The second line contains the length of side BC.
<br>
### Constraints:
```
* 0 < AB <= 100
* 0 < BC <= 100
* Lengths AB and BC are natural numbers.
```
<br>

### Output format:

Output angle `MBC` in degrees. 
Note: Round the angle to the nearest integer.
<br>

### Examples:
```
* If angle is 56.5000001°, then output 57°.
* If angle is 56.5000000°, then output 57°.
* If angle is 56.4999999°, then output 56°.
```
<br>

**Input:**
```
10
10
```
<br>

**Output:**
```
45°
```
<br>

## Solution 1

```python
# importing the module
import math

# taking the input from user
ab = float(input())
bc = float(input())

# finding the distance 
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

# equalizing the sides 
b = mc
c = bm
a = bc

# where b=c
# finding the angle in radian
angel_b_radian = math.acos(a / (2*b))

# converting the radian to degree
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# printing with degree
print(angel_b_degree,'\u00B0',sep='')
```
<br>

## Solution 2

```python
# importing the math module
import math

# taking input of the sides
ab=int(input())
bc=int(input())

# finding the distance
ca=math.hypot(ab,bc)
mc=ca/2

# finding the angle
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)

# printing the angle
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')
```
<br>

## Solution 3

```python
# importing math
import math

# taking inputs
a = int(input())
b = int(input())

# finding distace and angle
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M )

# printing the angle
print(int(round(math.degrees(theta),0)),'\u00B0',sep='')
```
<br>

## Solution 4

```python
# importing math
import math

# taking input from user
AB,BC=int(input()),int(input())

# calculating distance
hype=math.hypot(AB,BC)      

# calculating the angle
res=round(math.degrees(math.acos(BC/hype))) 

# the 176 represents the degree symbol
degree=chr(176)                          
print(res,degree, sep='')
```
<br>

