import requests

url = "https://jsonplaceholder.typicode.com/users"

for i in range(1,6):
    params = {
        "id" : i
        
    }
    

    response = requests.get(url, params=params)



    if response.status_code == 200:
        users = response.json()

        for user in users:
            print("ID:", user["id"])
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("-------------------")

    else:
        print("something went wrong")

    print(response.status_code, "\n")