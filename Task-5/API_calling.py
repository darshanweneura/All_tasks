import requests
def API_calling():
    url = "https://dps-007-default-rtdb.europe-west1.firebasedatabase.app/.json?print=pretty"

    response = requests.get(url)

    print(response.text)
    print(response.status_code)


API_calling()