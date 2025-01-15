# Strings p.s : All of subtopics of string in w3school is contained in this file except few that only was tet and no examples !

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Looping Through a String
for x in "Watermelon":
  print(x)

# String Length
c = "Hello, World!"
print(len(c))

# Check String
txt = "KBTU in hard yet Great!"
print("yet" in txt)



## Slicing Strings
d = "Hello, World!"
print(d[2:8])

## Slice From the Start
e = "Hello, Beautiful World!"
print(e[:5])

## Slice To the End
f = "Hello, Beautiful World!"
print(f[2:])

## Negative Indexing
g = "Hello, Beautiful World!"
print(g[-5:-2])



###  Modify Strings

### Upper Case
h = "Hello, World!"
print(h.upper())

### Lower Case

i = "Hello, World!"
print(i.lower())

### Remove Whitespace
j = " Hello, World! "
print(j.strip()) # returns "Hello, World!"

### Replace String
k = "Hello, World!"
print(k.replace("H", "J"))

### Split String
l = "Hello, World!"
print(l.split(",")) # returns ['Hello', ' World!']



#### String Concatenation
a1 = "Hello"
b1 = "World"
c1 = a1 + b1
print(c1)



##### Format - Strings
age = 18
txt = f"My name is Ehsan, I am {age}"
print(txt)
