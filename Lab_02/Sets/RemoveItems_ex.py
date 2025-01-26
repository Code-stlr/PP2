# Remove Set Items

# use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Or
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset
