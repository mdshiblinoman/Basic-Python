# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

'''
Why Use pass?
The pass statement is useful in several situations:
When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
'''
# During development, you might want to sketch out your program structure before implementing the details.
# The pass statement allows you to do this without syntax errors.
# Placeholder for future implementation:
age = 16
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

# Using pass in different branches:
value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

# Using pass with functions:
def calculate_discount(price):
  pass # TODO: Implement discount logic
# Function exists but doesn't do anything yet