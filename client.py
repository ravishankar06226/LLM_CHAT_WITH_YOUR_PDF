import requests

url = "http://127.0.0.1:8000"
query_string="Why choose python over R?"

response = requests.post(url, json={"question":query_string})

if response.status_code==200:
    print(response.json()["response"])
else:
    print(f"Error: {response.status_code} - {response.reason}")