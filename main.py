import requests

import json

# Create a function to get N th users

def get_user(n):

    url = f"https://randomuser.me/api/?results={n}"

    r = requests.get(url)

    return r.json()['results']

print(get_user(3))
    