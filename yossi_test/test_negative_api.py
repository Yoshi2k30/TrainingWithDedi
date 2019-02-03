import json
import requests

base_url = "http://localhost:1234"
list_url = base_url + "/list_not_there"
get_url = base_url + "/get"
save_url = base_url + "/save"

response = requests.request("GET", list_url)

assert response.status_code == 404

payload = {"Yosi": True}

response = requests.request("POST", save_url, data=json.dumps(payload))

assert response.status_code == 500

json_data = json.loads(response.content)

assert json_data == {'isError': True, 'message': '[True] is not a valid value, expecting type of ID.', 'statusCode': 500}
