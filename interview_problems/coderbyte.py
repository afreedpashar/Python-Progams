# Python CSV to JSON In the Python file, you have a program that performs a GET request on the route
# https://coderbyte.com/api/challenges/logs/user-info-csv and then sort the CSV data by the second column
# Finally, convert the sorted CSV data to a JSON object and print it. Be sure to call json.dumps on the final 
# object.
# Example Input:
# name,email,phone
# John Doe,johndoe@example.com,555-1234
# Jane Smith,janesmith@example.com,555-5678


# Example Output:
# [{"name":"John Doe","email":"johndoe@example.com","phone":"555-1234"},
#  {"name":"Jane Smith","email":"janesmith@example.com","phone":"555-5678"}]

import requests
import json
import csv
response = requests.get("https://coderbyte.com/api/challenges/logs/user-info-csv")
print(response)
if response.status_code == 200:
    csv_data=response.text.strip().split('\n')
    csv_reader=csv.reader(csv_data)
    sorted_csv=sorted(csv_reader, key=lambda row:row[1])
    headers = sorted_csv[0]
    json_data = [dict(zip(headers,row)) for row in sorted_csv[1:]]
    json_object = json.dumps(json_data, indent=2)
    print(json_object)
else:
    print("Failed to fetch the data")
