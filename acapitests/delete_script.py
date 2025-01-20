import requests

url = 'http://10.100.3.241/'
json_data = {'login': 'login12_super', 'password': '1Qwerty'}

ssid = requests.post(url + 'api/account/login', json=json_data).json()
headers = {'x-session-id': ssid['SID']}

#print(ssid)

for i in range(28, 100):
    res = requests.delete(url + f'api/hashsets/{i}', headers=headers)
    print(i, res.text)
# res = requests.post(url + f'api/hashsets', headers=headers, json=json_data)
# print(res.text)
requests.get(url + 'api/account/logout', headers=headers)