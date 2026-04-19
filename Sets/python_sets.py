'''
        Set:
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary,
all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
'''
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

'''
Set Items:
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered:
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable:
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
'''
'''
Duplicates Not Allowed:
Sets cannot have two items with the same value.
Duplicate values will be ignored:
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

'''
Get the Length of a Set:
To determine how many items a set has, use the len() function.
Get the number of items in a set:
'''
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)