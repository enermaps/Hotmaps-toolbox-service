import requests

from .. import BASE_URL

url = BASE_URL + "/users/login"

payload = {"email": "hotmapstest@gmail.com", "password": "weqriogvyx"}

resp = requests.post(url, json=payload)
if not resp.ok:
    raise Exception("Received an error upon login {}".format(resp.text))

test_token = resp.json()["token"]
