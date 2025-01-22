# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Using a While Loop

thislist2 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist2):
  print(thislist2[i])
  i = i + 1

# Looping Using List Comprehension
thislist3 = ["apple", "banana", "cherry"]
[print(x) for x in thislist3]