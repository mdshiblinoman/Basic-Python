# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

'''
Date Output:
When we execute the code from the example above the result will be:
2026-04-28 16:29:33.939734
The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date object.
Here are a few examples, you will learn more about them later in this chapter:
'''
# Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

'''
Creating Date Objects:
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
'''
# Create a date object:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

'''
The strftime() Method:
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
'''
# Display the name of the month:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

import datetime
x = datetime.datetime(2024, 8, 20)
print(x.strftime('%d'))