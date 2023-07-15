import requests
import json
import random
import string

from api.get import data

base_url = "https://gorest.co.in"
auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2ac6"

def get_request():
    url = base_url +"/public/v2/users/"
    print("get_url :" + url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data =response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body:" , json_str)


def generate_random_email():
    domain = "automation"
    email_leanth = 20
    random_string = ''.join(random.choice(string.ascii_lowercase)for _ in range(email_leanth))
    email = random_string +"@"+ domain
    return email

def post_request():
    url = base_url + "/public/v2/users/"
    print("post_url :" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "mohan",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response=requests.post(url,json=data,headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body:", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "mohan"
    return user_id


def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put_url :" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "mohan mademi",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "mohan mademi"

def delete_request():
    url = base_url + f"/public/v2/users/{user_id}"
    print("delete url :" + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200
    print(".....delete for user.....")




get_request()
user_id = post_request()
put_request(user_id)
delete_request()
# generate_random_email()