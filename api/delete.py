import requests

url = "https://reqres.in/api/users?page=2"

response=requests.delete(url)
print(response)