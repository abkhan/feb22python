import requests

url = "https://xkcd.com/info.0.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

