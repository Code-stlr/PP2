# Python Scope

# Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

# Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

## Two diffrent variable in two diff scopes 
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()
print(x)

# Global Keyword
# The global keyword makes the variable global.
def myfunc():
  global x
  x = 300

myfunc()
print(x)

# make change to global variable from inside the function 
x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)

# Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
# result : hello
