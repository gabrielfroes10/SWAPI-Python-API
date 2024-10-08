import requests

def fetch_data(endpoint):
    base_url = 'https://swapi.dev/api/'
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        return response.json()
    return None
