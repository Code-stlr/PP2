# Python Tuple
# A tuple is a collection which is ordered and unchangeable and allow duplicate values.
# mytuple = ("apple", "banana", "cherry")

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item
thistuple = ("apple",)
print(type(thistuple))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)