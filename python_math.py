# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)

# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print(x)

'''
The Math Module:
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module:
When you have imported the math module, you can start using methods and constants of the module.
The math.sqrt() method for example, returns the square root of a number:
'''
import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

import math
x = math.pi
print(x)
