# Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)

# Insert Items
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3)



## Add List Items
## Append Items
thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)

## Extend List
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)



### Remove List Items

list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)

# Remove Specified Index
remove1 = ["apple", "banana", "cherry"]
remove1.pop(1)
print(remove1)

remove2 = ["apple", "banana", "cherry"]
del remove2[0]
print(remove2)



# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

clearing = ["apple", "banana", "cherry"]
clearing.clear()
print(clearing)
