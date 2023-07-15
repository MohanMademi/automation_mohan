import requests
import json
import jsonpath


url = "https://reqres.in/api/users"

# Read file
file=open('C:\\Users\\madem\\OneDrive\\Documents\\post.json','r')
input_json = file.read()
request_json = json.loads(input_json)
print(input_json)

response = requests.put(url,request_json)
print(response.status_code)
print(response.content)
print(response.headers)
print(response.headers.get("Content-Length"))
print(response.headers.get("Connection"))

response_json = json.loads(response.text)
print(response_json)
put = jsonpath.jsonpath(response_json,"id")
print(put)
