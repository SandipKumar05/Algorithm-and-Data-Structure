import requests

url = 'https://www.example.com'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

url = 'https://www.example.com/search'
params = {'q': 'python', 'page': 1}
response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

url = 'https://www.example.com/api'
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=data)