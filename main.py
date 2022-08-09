import requests

def requesting_multiple_users(n:int)->list:
    # url for random user
    url = f'https://randomuser.me/api/?results={n}'
    # request
    r = requests.get(url) 
    #check status code
    if r.status_code == 200:
        # returs list cotainer n  users
        return r.json()['results']
    else:
        return []

if __name__ == '__main__':
    print(requesting_multiple_users(3))

