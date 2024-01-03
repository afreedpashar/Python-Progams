import requests

# API endpoint and key
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "3805f6bbabcb42b3a0c08a489baf603d"

# Parameters for the API request
params = {
    'country':'us',
    'apiKey':API_KEY
}
#making the api request
response = requests.get(API_URL,params=params)

#checking the request successsful
if response.status_code==200:
    print(response.json())
else:
    print(f"Error:{response.status_code}")