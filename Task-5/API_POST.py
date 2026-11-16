import requests

url = "https://jsonplaceholder.typicode.com/users"

student = {
    "id": 11,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "username": "rahul123"
}

response = requests.post(url, json=student)


print("Status:", response.status_code)
print("Response:", response.json())
