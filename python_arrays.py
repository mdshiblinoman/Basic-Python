# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

'''
What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
The solution is an array!
An array can hold many values under a single name, and you can access the values by referring to an index number.
Access the Elements of an Array
You refer to an array element by referring to the index number.
'''
# Get the value of the first array item:
x = cars[0]
print(x)

# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

# Return the number of elements in the cars array:
x = len(cars)
print(x)

# You can use the for in loop to loop through all the elements of an array.
# Print each item in the cars array:
for x in cars:
  print(x)

# You can use the append() method to add an element to an array.
# Add one more element to the cars array:
cars.append("Honda")
print(cars)

# You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array:
cars.pop(1)
print(cars)

# Delete the element that has the value "Volvo":
# cars.remove("Volvo")

# The append() method appends an element to the end of the list.
# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# Add a list to a list:
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)