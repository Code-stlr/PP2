# Python Iterators

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

