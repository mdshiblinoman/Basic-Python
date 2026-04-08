# Variables that are created outside of a function (as in all of the examples in the previous pages)
# are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

a = "awesome"
def myfunc():
  print("Python is " + a)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)
