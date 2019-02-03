import json
import requests

base_url = "http://localhost:1234"
list_url = base_url + "/list"
get_url = base_url + "/get"
save_url = base_url + "/save"

response = requests.request("GET", list_url)

assert response.status_code == 200
assert response.text == '{}'

payload = {"Yosi": 1234}

response = requests.request("POST", save_url, data=json.dumps(payload))

assert response.status_code == 200

response = requests.request("GET", list_url)

print(response.text)

assert response.status_code == 200
assert response.text == '{\'Yosi\': 1234}'

response = requests.request("GET", get_url+'/Yosi')

print(response.text)

assert response.status_code == 200
assert response.text == '{\'Yosi\': 1234}'
