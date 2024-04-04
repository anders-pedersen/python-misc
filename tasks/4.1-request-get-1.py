import requests
session = requests.Session()
r = session.get("https://httpbin.org/get")
print(f"r.text: {r.text}")     # feel free to comment this out
print(f"r.json(): {r.json()}") # feel free to comment this out

# your code goes here
print(f"Your public IP address is {r.json()['origin']}")
