import psycopg2
import csv
#Connectionn to database
conn = psycopg2.connect(host="localhost", dbname="phonebook",user="postgres", password="postgres", port=5432)
cur = conn.cursor()
#table creation
cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            phone BIGINT NOT NULL
            );
            """)

user_choice = int(input("Select the number of action you want to do :\n"
"1)Insert data (from CSV)\n" 
"2)Insert data (Manual)\n" 
"3)Insert data(MultipleAtOnce)\n"
"4)Update data\n" 
"5)Query\n" 
"6)Query(Limit&Offset)\n"
"7)Delete Data\n"
"8)Seach by part\n"
"9)Delete All table content\n"
"Select :"))
# resets the id to 1 if table is empty
def reset_sequence_if_empty():
    cur.execute("SELECT COUNT(*) FROM phonebook")
    row_count = cur.fetchone()[0]

    if row_count == 0:
        cur.execute("ALTER SEQUENCE phonebook_id_seq RESTART WITH 1")
#functions 
def insert_csv():
  reset_sequence_if_empty()
  
  with open(r'C:\My Web Sites\pp2\Lab_11_v2\phonebook.csv', 'r') as file:
    data_reader = csv.reader(file)
    next(data_reader)
    for row in data_reader:
        cur.execute("""INSERT INTO phonebook (name, phone)  VALUES (%s, %s)""", row)
  print("Insert successful!")
def insert_manual():
  reset_sequence_if_empty()
  name_input = input("Enter name: ")
  phone_input = int(input("Enter phone number: "))

  cur.execute("""SELECT EXISTS (SELECT 1 FROM phonebook WHERE name=%s);""", (name_input,))
  Chekcer = cur.fetchone()[0]
  if Chekcer:
    cur.execute("""UPDATE phonebook SET phone=%s WHERE name=%s""",(phone_input, name_input))
  else:
    cur.execute("""
        INSERT INTO phonebook(name, phone) VALUES (%s, %s)
        """, (name_input, phone_input)
    )
  print("input successful")
def insert_multiple():
  reset_sequence_if_empty()
  print("In here you can insert multiple records into the table\n")
  counter = int(input("How many person ? "))
  for i in range(0, counter):
    name_input = input(f"Enter name for person {i + 1}: ")
    phone_input = int(input(f"Enter phone number for person {i + 1}: "))
    cur.execute("""INSERT INTO phonebook (name, phone) VALUES (%s, %s)""", (name_input, phone_input))
  print("Insert Successful!")
def update():
  id_to_update = input("Enter the ID of the record to update: ")
  choice_input = int(input("Update 1)Name or 2)Phone number ? "))
  if choice_input == 1:
    name_input = input("Enter new name: ")
    cur.execute(""" UPDATE phonebook SET name = %s WHERE id = %s
     """, (name_input, id_to_update))
    print("Update successful!")
  elif choice_input == 2:
    phone_input = int(input("Enter new phone number: "))
    cur.execute("""UPDATE phonebook SET phone = %s WHERE id = %s""", (phone_input, id_to_update))
    print("Update successful!")
  else:
    print("Enter a valid number")
def query():
  cur.execute("SELECT COUNT(*) FROM phonebook")
  row_count = cur.fetchone()[0]
  if row_count == 0:
    print("Table is empty!")
  else:
    cur.execute("SELECT * FROM phonebook")
    for records in cur.fetchall():
      print(records)
def queryPag():
  limit = int(input("Size of page (limit)? "))
  page = int(input("Which page you need ? "))
  offset = limit * (page-1)
  cur.execute("""SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s""",(limit, offset))
  for records in cur.fetchall():
    print(records)
def deletedata():
  query()
  user_input = int(input("Delete by 1)name or 2)phone number?"))
  if user_input == 1:
    names = input("Enter name (seperated by comma): ").split(',')
    for name in names:
      name = name.strip()
      cur.execute("""DELETE FROM phonebook WHERE name=%s""", (name,))
  elif user_input == 2:
    numbers = input("Enter the numbers (separated by comma): ").split(',')
    for number in numbers:
      number = int(number)
      cur.execute("""DELETE FROM phonebook WHERE phone=%s""",(number,))
  else:
    print("Invalid input! try again")
  print("Delete successful!")
def searchByParts():
  user_input = int(input("You want to search by 1)name or 2)phone number? "))
  if user_input == 1:
    namepart = input("Enter the part of the name: ")
    cur.execute("""SELECT * FROM phonebook WHERE name ILIKE %s""", ('%' + namepart + '%',))
    result = cur.fetchall()
    for i in result:
      print(i)
  elif user_input == 2:
    phonepart = int(input("Enter the part of the phone number: "))
    cur.execute("""SELECT * FROM phonebook WHERE phone ILIKE %s""", ('%' + phonepart + '%',))
    result = cur.fetchall()
    for i in result:
      print(i)
  else:
    print("Invalid input! Please try again.")   
#extra function
def deleteAll():
  confirmation = input("Are you sure you wanna delete all the data inside the table ? yes/no ")
  if confirmation.lower() == 'yes':
    cur.execute("""TRUNCATE TABLE phonebook""")
    print("Deleted!")
  elif confirmation.lower() == 'no':
    print("Deletion cancelled.")
  else:
    print("Invalid input! Please type 'yes' or 'no'.")
if 1 <= user_choice <= 9:
  if user_choice == 1:
    insert_csv()
  elif user_choice == 2:
    insert_manual()
  elif user_choice == 3:
    insert_multiple()
  elif user_choice == 4:
    update()
  elif user_choice == 5:
    query()
  elif user_choice == 6:
    queryPag()
  elif user_choice == 7:
    deletedata()
  elif user_choice == 8:
    searchByParts()
  elif user_choice == 9:
    deleteAll()
else:
  print("invalid input")

#commit and close
conn.commit()
cur.close()
conn.close()