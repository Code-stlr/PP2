# Python RegEx

# RegEx Module
import re
# Example
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# The findall() Function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The search() Function
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# The split() Function
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# The sub() Function
# Replaces characters
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
 