a = [106, 117, 115, 116, 95, 119, 97, 114, 109, 105, 110, 103, 95, 117, 112]
flag = "".join([chr(x) for x in a])


import requests

headers = {
    'Content-type': 'application/json',
}

data = '{"pass": "just_warming_up"}'

response = requests.post('http://ctf.securityvalley.org:7777/api/v1/validate', headers=headers, data=data)

print(response.json())
