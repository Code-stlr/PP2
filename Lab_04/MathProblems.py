import math
#Probelm 1

n = int(input())

print(math.radians(n))

# Probelm 2
h = int(input("Height: "))
a = int(input("1st base: "))
b = int(input("2nd base: "))

print(((a + b) / 2) * h)
# Problem 3
n = int(input("Number of sides: "))
s = float(input("Length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(round(area, 3))

# Problem 4
b = int(input("base: "))
h = int(input("height: "))

print(h * b)
