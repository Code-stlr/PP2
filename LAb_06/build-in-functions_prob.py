import math 
import time

# problem 1
someList = [1, 2, 3, 4, 5]
mul = math.prod(someList)
print(f"Product of the numbers indide the list is : {mul}")

# Problem 2
sentence = input("Gimme a sentence : ")
words = sentence.split()
uppercase_cnt = 0
lowercase_cnt = 0
for i in words:
  for j in i:
    if j.isupper():
      uppercase_cnt += 1
    else:
      lowercase_cnt += 1
print(f"Number of uppercase letters : {uppercase_cnt}")
print(f"Number of lowercase letters : {lowercase_cnt}")

# probelm 3
word = input("Give me a word : ")
temp = (word == word[::-1])
if temp:
  print(f"{word} is palindrom")
else:
  print(f"{word} is not a palindrom")

# Problem 4
num = int(input("Enter a number: "))
ms = int(input("Enter delay in milliseconds: "))
time.sleep(ms / 1000)
result = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {result}")

# Problem 5
tuple1 = (True, False, True)
tuple2 = (True, True)
print(all(tuple1))
print(all(tuple2))