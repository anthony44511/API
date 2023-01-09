import requests

response = requests.get("https://randomuser.me/api/")
request = response.request

print(response.text)
print(request.path_url)