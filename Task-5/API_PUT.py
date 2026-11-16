import requests

url = "https://jsonplaceholder.typicode.com/users/1"

update = {
    "id": 1,
    "name": "Darshan",
    "email": "dps@gmail.com"
}

response = requests.put(url,json=update)

print(response.status_code)
print(response.json())

