# Python JSON
# JSON is a syntax for storing and exchanging data.
import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON
# using the json.dumps() method.


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# Format the Result
json.dumps(x, indent=4)
# or use seperators 
json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result (Sorting)
json.dumps(x, indent=4, sort_keys=True)
