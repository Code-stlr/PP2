# user number
# class number
# function 2: prime, odd/even
# min 3

class Number:
  def __init__(self):
    self.number = 0
  def input(self):
    self.number = int(input("Enter a number: "))

  def prime(self):
    counter = 0
    if self.number > 1:
      for i in range(1, self.number + 1):
        if self.number % i == 0:
          counter += 1
      if counter > 2:
        print("Number is not prime !")
      else:
        print("Number is prime !")
    else:
      pass
  def oddEven(self):
    if self.number % 2 == 0:
      print("Number is even !")
    else:
      print("Number is odd !")

p1 = Number()
p1.input()
p1.prime()
p1.oddEven()