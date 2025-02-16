# Python Modules
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:
def greeting(name):
  print("Hello, " + name)

# Use a Module
import mymodule

mymodule.greeting("Jonathan")
# use the syntax: module_name.function_name.

# Variables in Module
# code inn module 
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)
#result : 36

# Re-naming a Module
# Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
import platform

x = platform.system()
print(x)

# Using the dir() Function
import platform

x = dir(platform)
print(x)

# # Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print (person1["age"])