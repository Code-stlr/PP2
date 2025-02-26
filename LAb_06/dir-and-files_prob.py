import os 
import string

#Probelm 1
pathHolder = input("What the path ? ")

if os.path.exists(pathHolder) and os.path.isdir(pathHolder):
  directories = [d for d in os.listdir(pathHolder) if os.path.isdir(os.path.join(pathHolder, d))]
  files = [f for f in os.listdir(pathHolder) if os.path.isfile(os.path.join(pathHolder, f))]

  print("Directories:", directories)
  print("Files:", files)
  print("All contents:", os.listdir(pathHolder))
else:
  print("The specified path is not a directory or does not exist.")


#Probelm 2
pathHolder = input("What the path ? ")
if os.path.exists(pathHolder):
  print("The path exists.")
  print(f"Readable: {'Yes' if os.access(pathHolder, os.R_OK) else 'No'}")
  print(f"Writable: {'Yes' if os.access(pathHolder, os.W_OK) else 'No'}")
  print(f"Executable: {'Yes' if os.access(pathHolder, os.X_OK) else 'No'}")
else:
  print("Path does not exist")

#Problem 3
pathHolder = input("What the path ? ")
if os.path.exists(pathHolder):
  print("Such path exists !")
  directory = os.path.dirname(pathHolder)
  filename = os.path.basename(pathHolder)
  print(f"Directory: {directory}")
  print(f"Filename: {filename}")
else:
  print("Path does not exist")

#Problem 4
with open(r"C:\My Web Sites\pp2\LAb_06\lorem_txt.txt", 'r', encoding='utf-8') as txt:
  counter = 0
  for i in txt:
    counter += 1
  print(f"Number of lines in txt file: {counter}")

#Problem 5
with open(r"C:\My Web Sites\pp2\LAb_06\lorem_txt.txt", 'w', encoding='utf-8') as txt:
  ourList = ['Hello World', 123, "456", 200]
  for i in range(0, len(ourList)):
    txt.write(str(ourList[i]) + '\n')
    
# Problem 6
string.ascii_uppercase # this is our alphabet 
alphabet = list(string.ascii_uppercase)
cnt = 26
try:
  for i in range(0, cnt):
    newFile = open(f"{alphabet[i]}.txt", 'x')
except:
  print("There is some file created by that name already !")

# Problem 7
def Duplicator():
  try:
    txt = open(r"C:\My Web Sites\pp2\LAb_06\lorem_txt.txt", 'r', encoding='utf-8')
    tempHolder = txt.read()
    FileName = input("What the new file name ?: ")
    newFile = open(f"{FileName}.txt", 'x')
    newFile.write(tempHolder)
  except:
    print("There exist some file by the same name!!")
    Duplicator()
Duplicator()

# Probelm 8
pathHolder = input("What the path ? ")
if os.path.exists(fr"{pathHolder}"):
  os.remove(fr"{pathHolder}")