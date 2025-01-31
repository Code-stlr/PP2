from itertools import permutations
#problem 1
grams = int(input("How many grams do you ned ? "))

def GramsToOunces(grams):
  ounces = 28.3495231 * grams
  print(ounces, "Ounces !")

GramsToOunces(grams)

#problem 2
fahrenheit = int(input("Whats the temp ?"))

def FtoC(fahrenheit):
  print(int((5/9) * (fahrenheit - 32)))

FtoC(fahrenheit)

#problem 3
heads =int(input("Number of heads : "))
legs = int(input("Number of legs : "))
def solev(numheads, numlegs):
  y = (numlegs - 2 * numheads) // 2
  x = numheads - y
  if x < 0 or y < 0 or 2*x + 4*y != numlegs:
    return "No solution"
  print(f"Chickens: {x}, Rabbits: {y}")
solev(heads, legs)
#problem 4
YOYOYO = int(input("How many numbers ? "))
numbers = [int(input("Enter a number ")) for i in range(YOYOYO)]
def Prime(ListOfNumbers):
  i = 2
  for x in ListOfNumbers:
    sum = 0
    for y in range(1, x+1):
      if x % y == 0:
        sum += 1
    if sum == i:
      print(x, "is a prime number")

Prime(numbers)

# problem 5
def print_permutations(input_string):
    perms = [''.join(p) for p in permutations(input_string)]
    
    
    for perm in perms:
        print(perm)


user_input = input("Enter a string: ")
print_permutations(user_input)

# problem 6 
sentence = input("enter you sentence : ")

def reverse(sentence):
  somelist = sentence.split()
  somelist.reverse()
  for i in somelist:
    print(i)
reverse(sentence)

# problem 7
def has_33(nums):
  situation = False
  for i in range(len(nums)-1):
    if nums[i] == 3 and nums[i] == nums[i+1]:
      situation = True
  return situation

print(has_33([1, 3, 1, 3]))


#problem 8
def spy_game(nums):
  situation = False
  for i in range(len(nums)-2):
    if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
      situation = True
  return situation

print(spy_game([1,0,2,4,0,5,7]))

# problem 9
radius = float(input("What is the radius of the circle ? "))
def volumeFinder(radius):
  volume = (4/3 ) * 3.1416 * (radius ** 3) #considering pi as 3.1416
  return volume

print(volumeFinder(radius))

# problem 10
count = int(input("How many elements in the list ? "))
numbers = []
for i in range(count):
  numbers.append(int(input("Enter a number: ")))

def unique_sorter(list, count):
  new_list = []
  for i in range(count): 
    if list[i] in new_list:
      pass
    else:
      new_list.append(list[i])
  for i in new_list:
    print(i)

unique_sorter(numbers, count)

#problem 11
word = input("Enter a word : ")
def palindrom(word):
  if word == word[::-1]:
    print("It is palindrom !")
  else:
    print("It is not palindrom :(" )
palindrom(word)

#problem 12

count = int(input("How many elements in the list ? "))
numbers = []
for i in range(count):
  numbers.append(int(input("Enter a number: ")))

def histogram(numbers):
  for i in numbers:
    print(i * "*")
histogram(numbers)

#prblem 13
import random
name = input("Hello! What is your name? ")
print()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
number = random.randint(1, 20)
run = True
guess_counter = 0
while run:
  guess = int(input("Take a guess."))
  if guess > number:
    print("Your guess is too high.")
    guess_counter += 1
  elif guess < number:
    print("Your guess is too low.")
    guess_counter += 1
  else:
    print(f"Good job, {name}! You guessed my number in {guess_counter + 1} guesses!")
    guess_counter = 0
    run = False
