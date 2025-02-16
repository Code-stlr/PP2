import json

# Use an absolute path to the JSON file
file_path = r"C:\My Web Sites\pp2\Lab_04\sample-data.json"

# Open and read the JSON file
with open(file_path, "r") as f:
    data = json.load(f)

print("======================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-------------------------------------------------- ------------------- ------- -----")

# Extract "imdata" list
data_list = data.get("imdata", [])

# Iterate through the data
for item in data_list:
    l1_Phys_If = item.get('l1PhysIf', {}).get('attributes', {})
    dn = l1_Phys_If.get('dn', '')
    desc = l1_Phys_If.get('descr', 'N/A')  # Provide a default value
    speed = l1_Phys_If.get('speed', 'N/A')
    mtu = l1_Phys_If.get('mtu', 'N/A')

    print(f"{dn:<50}{desc:<22}{speed:<10}{mtu:<6}")
