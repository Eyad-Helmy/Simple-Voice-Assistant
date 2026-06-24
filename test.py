import requests
from urllib.parse import quote_plus

location = "cairo" or ""
query = quote_plus(location) if location else ""
url = f"https://wttr.in/{query}?format=j1"

data = requests.get(url)
# print(dir(data))
# print(data.content)
# print(data._content)
print(data.json()["current_condition"])