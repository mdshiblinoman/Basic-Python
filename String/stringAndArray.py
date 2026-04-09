'''
Strings are Arrays
    Like many other popular programming languages, strings in Python are arrays of unicode characters.
    However, Python does not have a character data type, a single character is simply a string with a length of 1.
    Square brackets can be used to access elements of the string.
'''
a = "Hello, World!"
print(a[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)

# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")