# Problem 
n = int(input())

def generate_squares(n):
    squares = []
    for i in range(n + 1):
        squares.append(i**2)
    return squares

print(generate_squares(n))



# Problem 2
n = int(input())

def even_numbers(n):
    even_nums = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

nums = even_numbers(n)
print(*nums, sep=', ')

# Probleme 3
def divisible_by3and4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print(*divisible_by3and4(30), sep=", ")

# Problem 4
left = int(input("Left bound: "))
right = int(input("Right bound: "))

def squares(left, right):
    for i in range(left, right + 1):
        yield i ** 2

print(*squares(l, r), sep=', ')

# Problem 5
n = int(input())

def nums(n):
    for i in range(n, -1):
        yield i

print(*nums(n))