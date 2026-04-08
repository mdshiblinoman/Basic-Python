# The print() function is often used to output variables.
a = "Python is awesome"
print(a)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
d = "Python "
e = "is "
f = "awesome"
print(d + e + f)

# For numbers, the + character works as a mathematical operator:
g = 10
h = 20
print(g+h)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
print(x, g)