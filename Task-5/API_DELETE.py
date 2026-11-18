import requests as rq

url = "https://jsonplaceholder.typicode.com/users/1"

res = rq.delete(url)

print(res.status_code)
if res.status_code == 200:
    print("delete successfully!")
else:
    print("somwthing went wrong")