import json
import re

# Open the input JSON file
with open('sampleData.json', 'r') as f:
    data = json.load(f)

date_regex = re.compile(r'(\d{8})|(\d{4}-\d{2}-\d{2})')

# Loop over each object in the JSON file
for obj in data:

    if obj.split('_')[2].isdigit():
        time = obj.split('_')[2][:4] # Extract the time from the property name
    else:
        time = obj.split('_')[1] # Extract the time from the property name
    data[obj]['time'] = time
    print(obj)
    print(time)

    # match = date_regex.search(obj)
    # if match:
    #     date = match.group()
    #     # Format the date to YYYYMMDD
    #     date = re.sub(r'[-]', '', date)
    # #     print(date)
    # # else:
    # #     print(f"No date found in {obj}")
    # # # Add a "date" attribute to the object
    # data[obj]['date'] = date


    # string = obj
    # start = string.find("[") + 1
    # end = string.find("]")
    # x, y = string[start:end].split()
    # # Add a "location" attribute to the object
    # data[obj]['location'] = [float(x), float(y)]

# Write the modified JSON data back to the file
with open('output.json', 'w') as f:
    json.dump(data, f)
