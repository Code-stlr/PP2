# Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# Or do it by index
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0

while i < len(thistuple):
  print(thistuple[i])
  i += 1

