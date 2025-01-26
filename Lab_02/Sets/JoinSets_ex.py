# Join Sets

# Union
# You can use the | operator instead of the union() method

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# set3 = set1 | set2
print(set3)

# Join Multiple Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 |set4
print(myset)


# Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Intersection
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
# set3 = set1 & set2
print(set3)

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
# set3 = set1 - set2
print(set3)


# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
print(set3)