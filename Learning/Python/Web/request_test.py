import requests
url = 'https://malbuffer4pt.github.io'
response = requests.get(url=url)
print(response.text)

data = {
    'data':123456,
    'password':123456
}
response = requests.post(url=url, data=data)
print(response.text)