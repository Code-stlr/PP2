# Global Variables

x = "awesome"

def KBTU():
  print("KBTU is " + x)

KBTU()
### 2nd example
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("KBTU is " + x)

# The global Keyword
def myfunc2():
  global x
  x = "fantastic"

myfunc()

print("KBTU is " + x)


## 
x = "hard"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("KBTU is " + x)