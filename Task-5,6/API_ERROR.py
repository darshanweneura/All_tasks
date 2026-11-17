import requests as rq

url = "https://temporary-data-3776-default-rtdb.asia-southeast1.firebasedatabase.app/users.json?print=pretty"

try:
    response = rq.get(url,timeout=10)
    
    response.raise_for_status()
    
    users = response.json()

    for user in users.values():
        print(user["name"])
        
except rq.exceptions.Timeout:
    print("request time out")
except rq.exceptions.HTTPError as e:
    print("HTTP error",e)
except ValueError:
    print("Invalid JSON response!")