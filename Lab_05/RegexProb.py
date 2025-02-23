import re
txt = open(r'C:\My Web Sites\pp2\Lab_05\row.txt', 'r', encoding ='utf-8')

for i, line in enumerate(txt, 1):
  line = line.rstrip()
  if re.findall(r'а[б0]', line):
    print(f"Line number : {i}, line: {line}")

# Problem 2
for i, line in enumerate(txt, 1):
  line = line.rstrip()
  if re.findall(r'аб{2,3}', line):
    print(f"Line number : {i}, line: {line}")

# Problem 3
for i, line in enumerate(txt, 1):
  line = line.rstrip()
  matches = re.findall(r'[а-я]+_[а-я]+', line)
  for match in matches:
    print(i, match)

# Problem 4
for i, line in enumerate(txt, 1):
  line = line.rstrip()
  matches = re.findall(r'\b[А-Я][а-я]+\b', line)
  for match in matches:
    print(f"Line number {i}, match : {match}")

# Problem 5
for i, line in enumerate(txt, 1):
  line = line.strip()
  if re.search(r'а.*\s*б$', line):
    print(f"Line {i}: {line}")

# Problem 6
temp = txt.read()
new_txt = re.sub(r"[ ,.]", ":", temp)
file = open(r'C:\My Web Sites\pp2\Lab_05\changedtxt.txt', 'w', encoding='utf-8')
file.write(new_txt)

# Problem 7
def snake_to_camel(txt):
    words = txt.split('_')
    c_words = words[0].capitalize() + ''.join(word.capitalize() for word in words[1:])
    return c_words    
    
print(snake_to_camel(txt))

# Problem 8
def space_between_big(txt):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return result

print(space_between_big(txt))

# Problem 9
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)


result = insert_spaces(txt)
print(result)

# Probelm 10
def camel_to_snake(txt):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', txt)
    return result
    
print(camel_to_snake(txt))