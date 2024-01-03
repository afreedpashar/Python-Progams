import requests
import json

url = requests.get('https://jsonplaceholder.typicode.com/users/1')
response_json = json.loads(url.text)
print(response_json)
# for todo in response_json:
#     if todo['id'] == 5:
#         print(todo['title'])