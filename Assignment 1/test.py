import requests

params = {
"_id": 1200
}

r = requests.post(url="http://34.134.176.176:5000/wait", json=params)

print(r.text)