# Sort Lists
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)

# Sort Descending
R_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
R_list.sort(reverse = True)
print(R_list)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key = myfunc)
print(thislist2)


#  case-insensitive sort function:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)