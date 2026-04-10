'''
Slicing
    You can return a range of characters by using the slice syntax.
    Specify the start index and the end index, separated by a colon, to return a part of the string.
'''

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# By leaving out the start index, the range will start at the first character:
a = "Hello, World!"
print(a[:5])

# By leaving out the end index, the range will go to the end:
x = "Hello, World!"
print(x[2:])

# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])