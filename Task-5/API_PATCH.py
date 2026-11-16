import requests as rq

url = "https://jsonplaceholder.typicode.com/users/1"

update = {
    "email":"dps@gmail.com"
}

res = rq.patch(url,json=update)

print(res.status_code)
print(res.json())