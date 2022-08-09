import requests

# url for randomuser
URL = "https://randomuser.me/api/"

def get_users(n: int) -> list:
    # create query request
    url = f"{URL}/?results={n}"
    # get request
    response = requests.get(url)

    if response.status_code == 200:
        # get users
        users = response.json()['results']
        return users
    
    return []