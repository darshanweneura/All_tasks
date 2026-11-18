import requests as r
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = r.get(url,timeout=10)
    response.raise_for_status()
    users = response.json()

    with open (r"E:\Darshan_Weneura\Task-5\users.json","w") as file:
        json.dump(users,file,indent=4)
    print("API data saved into JSON file!")

except r.exceptions.RequestException as e:
    print("API Error:", e)
except (OSError, TypeError) as e:
    print("File Error:", e)