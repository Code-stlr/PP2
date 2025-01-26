# Access Dictionary Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# or
x = thisdict.get("model")


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)


# Get Values
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
