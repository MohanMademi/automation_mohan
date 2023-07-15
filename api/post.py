import requests
import json
import jsonpath

#
# url = "https://reqres.in/api/users"
#
# # Read file
# file=open('C:\\Users\\madem\\OneDrive\\Documents\\post.json','r')
# input_json = file.read()
# request_json = json.loads(input_json)
# print(input_json)
#
# response = requests.post(url,request_json)
# print(response.status_code)
# print(response.content)
# print(response.headers)
# print(response.headers.get("Content-Length"))
# print(response.headers.get("Connection"))
#
# response_json = json.loads(response.text)
# print(response_json)
# post = jsonpath.jsonpath(response_json,"id")
# print(post)
# print






#
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# print(response.json())
# # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
#
# print(response.status_code)
#





#
# import requests
# import json
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# print(response.json())
# # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
#
# print(response.status_code)

