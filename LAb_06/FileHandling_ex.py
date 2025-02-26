# Python File Open
# The key function for working with files in Python is the open() function.
# "r" - Read 
# "a" - Append
# "w" - Write 
# "x" - Create
# "t" - Text 
# "b" - Binary 

f = open("demofile.txt")


##Read File 
f = open("demofile.txt", "r") # demofile.txt is the name of the txt file
print(f.read())

# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
f = open("demofile.txt", "r")
print(f.readline())

# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)



### Write/Create file 
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile2.txt", "r") #open and read the file after the appending:
print(f.read())


# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist
f = open("myfile.txt", "w")



#### Python Delete Files 
# Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

# Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Delete Folder
os.rmdir("myfolder")

# Close Files
f = open("demofile.txt", "r")
f.close()