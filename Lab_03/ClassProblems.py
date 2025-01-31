# problem 1
class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Example usage:
handler = StringHandler()
handler.getString()  # User inputs a string
handler.printString()  # Prints the string in uppercase

# probelm 2

class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2  

shape = Shape()
print("Shape area:", shape.area())  # Output: 0

square = Square(5)
print("Square area:", square.area())  # Output: 25


# problem 3

class Shape:
    def area(self):
        return 0 

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
    
rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())  # Output: 24


# problem 4
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
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")


account = Account("John Doe", 100)

account.withdraw(30)   # Withdrew: $30. New balance: $120
account.withdraw(200)  # Insufficient funds!
account.deposit(-10)   # Deposit amount must be positive.
account.withdraw(-5)   # Withdrawal amount must be positive.

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
