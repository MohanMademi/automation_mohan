# What is API testing?
# API testing is a type of software testing that focuses on testing the functionality, performance, and security of APIs (Application Programming Interfaces).
#
# How do you perform API testing in Python?
# API testing in Python can be performed using libraries such as requests, unittest, pytest, or specialized libraries like RestAssured and HTTPie.
#
# What is the requests library in Python used for?
# The requests library is a popular Python library used for making HTTP requests to interact with APIs. It provides a simple and intuitive API for sending HTTP requests and handling responses.
#
# How do you send GET requests using the requests library in Python?
# You can send GET requests using the requests.get() method. Here's an example:

# python
# Copy code
import requests

response = requests.get("https://api.example.com/users")
print(response.status_code)
print(response.json())
# How do you send POST requests using the requests library in Python?
# You can send POST requests using the requests.post() method. Here's an example:
# python
# Copy code
import requests

data = {"username": "john", "password": "pass123"}
response = requests.post("https://api.example.com/login", json=data)
print(response.status_code)
print(response.json())
# How do you handle authentication in API testing using the requests library in Python?
# You can handle authentication by including the appropriate headers or using authentication schemes like Basic or OAuth. Here's an example using Basic authentication:
# python
# Copy code
import requests
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.example.com/secure-endpoint", auth=HTTPBasicAuth("username", "password"))
print(response.status_code)
print(response.json())
# How do you handle query parameters in API testing using the requests library in Python?
# You can include query parameters by passing them as a dictionary in the params parameter of the request methods. Here's an example:
# python
# Copy code
import requests

params = {"page": 1, "limit": 10}
response = requests.get("https://api.example.com/users", params=params)
print(response.status_code)
print(response.json())
# How do you handle headers in API testing using the requests library in Python?
# You can include headers by passing them as a dictionary in the headers parameter of the request methods. Here's an example:
# python
# Copy code
import requests

headers = {"Authorization": "Bearer token123"}
response = requests.get("https://api.example.com/users", headers=headers)
print(response.status_code)
print(response.json())
# How do you perform assertions in API testing using Python?
# You can use assertion libraries like unittest or pytest to perform assertions on the API responses. Here's an example using unittest:
# python
# Copy code
import unittest
import requests

class APITest(unittest.TestCase):
    def test_get_users(self):
        response = requests.get("https://api.example.com/users")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

if __name__ == "__main__":
    unittest.main()
# How do you handle JSON parsing in API testing using Python?
# The requests library automatically parses JSON responses into Python objects. You can access the JSON data using the .json() method. Here's an example:
# python
# Copy code
import requests

response = requests.get("https://api.example.com/users")
data = response.json()
print(data["name"])
print(data["email"])
# These are some of the common interview questions and answers for API testing with Python. You can explore more advanced topics like handling authentication tokens, handling cookies, or performing API test automation using frameworks like pytest or Swagger UI integration.