import requests
import jsonpath
import json
#
# url = "https://reqres.in/api/users?page=2"
#
# response=requests.get(url)
#
#
# json = json.loads(response.text)
# # print(json)
#
# data = jsonpath.jsonpath(json,'total_pages')
# print(data[0])
# assert data[0] == 2






import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()
print(response.status_code)
print(response.headers["Content-Type"])