# Unpack Tuples

fruits = ("apple", "banana", "cherry") # A packed tuple !

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# The number of variables must match the number of values in the tuple


# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# add an * to the variable name and the values will be assigned to the variable as a list