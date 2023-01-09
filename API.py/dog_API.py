import requests
import os
os.system('cls')

response = requests.get("https://api.thedogapi.com/")
request = response.request

print(response.text)
print(request.headers)
print(response.status_code)
print(response.headers)