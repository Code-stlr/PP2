# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)

#example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# example 3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# Some Values are False
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

# Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction())