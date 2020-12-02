import requests
import url_call

url = url_call.url()

response = requests.get(url)
print(response.json())

