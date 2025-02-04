# problem 1
class getStringYo():
  def __init__(self):
    self.text = " "
  def getString(self):
    self.text = input("Enter a sentence : ")
  def printString(self):
    print(self.text.upper())

p1 = getStringYo()
p1.getString()
p1.printString()

# problem 2

class Shape:
  def area(self):
    print(0)

class Square(Shape):
  def __init__(self, length):
    self.length = length
  def area(self):
    print(self.length ** 2)

shape = Shape()
shape.area()
square = Square(5)
square.area()

# problme 3
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    print(self.length * self.width)
rectangle = Rectangle(2,5)
rectangle.area()  

# # problem 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()  # Output: (3, 4)
p2.show()  # Output: (6, 8)

print("Distance:", p1.dist(p2))  # Output: 5.0

p1.move(10, 12)
p1.show()  # Output: (10, 12)


# problem 5
class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def deposit(self):
    temp = int(input("How much to deposit ? "))
    self.balance += temp
    print("Balance : ", self.balance)
  def withdraw(self):
    temp = int(input("How much to withdraw ? "))
    if temp > self.balance:
      print("Not enough balance!")
    else:
      self.balance -= temp
      print("Remains : ", self.balance)

p1 = Account("Ehsan", 1000)
#for testing
p1.deposit()
p1.deposit()
p1.withdraw()
p1.withdraw()

# problem 6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 25]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)