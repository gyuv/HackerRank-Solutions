# Polar coordinates

## Task:
You are given a complex z. Your task is to convert it to polar coordinates.

Polar coordinates are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number)

A complex number `z`
`z = x + yj`

is completely determined by its real part `x` and imaginary part `y`.
Here, `j` is the [Imaginary Unit](https://en.wikipedia.org/wiki/Imaginary_unit).

A polar coordinate `(r, q)`
is completely determined by modulus `r` and phase angle `q`.

if we convert complex number `z` to its polar coordinate, we find:
`r` : Distance from `z` to origin, i.e.,`√(x^2+y^2)`
`q` : Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.

Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.

`cmath.phase`
This tool returns the phase of complex number `z`(also known as the argument of `z`).


```
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```

abs
This tool returns the modulus (absolute value) of complex number `z`.

```
>>> abs(complex(-1.0, 0.0))
1.0
```
<br>
### Input Format

A single line containing the complex number `z`. Note: complex() function can be used in python to convert the input as a complex number.


<br>

### Constraints
* Given number is a valid complex number

<br>

### Output Format

* Output two lines:
* The first line should contain the value of `r`.
* The second line should contain the value of `q`.


<br>



**Sample Input**



```
 1+2j
```

<br>


**Sample Output**


```
2.23606797749979 
1.1071487177940904
```


<br>


**Explanation**

* This Python code demonstrates the use of the `cmath` module to convert a complex number to its polar representation, i.e., magnitude and phase.

* The first line imports the cmath module, which provides mathematical functions for complex numbers.

* The second line prompts the user to input a complex number and creates a complex object num from the input.

* The third line creates a new complex object `z` with the same value as `num`.

* The fourth line uses the `cmath.polar()` function to compute the polar coordinates of `z`. The function returns a `tuple` containing the magnitude and phase of the complex number, respectively.

* The fifth line prints the magnitude of `z`, which is the first element of the tuple returned by `cmath.polar()`.

* The sixth line prints the phase of `z`, which is the second element of the tuple returned by `cmath.polar()`.

<br>

## Solution

```python
import cmath;

num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])

```
