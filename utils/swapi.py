import json
import os
from urllib.parse import urlparse, parse_qs
import requests
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
dir = os.path.join(parent_dir, 'endpoints')
sys.path.append(dir)

from endpoints import endpoints_starwars

def getpeople(id=None):
    if id is not None:
        url = f"{endpoints_starwars.endpoints.people}{id}"
    else:
        url = f"{endpoints_starwars.endpoints.people}"
    response = requests.get(url)
    return response


def get_all_people():
    all_people = []
    next_url = None

    response = getpeople()
    data = response.json()

    all_people.extend(data['results'])

    if 'next' in data:
        next_url = data['next']

    while next_url:
        parsed_url = urlparse(next_url)
        query_params = parse_qs(parsed_url.query)
        next_page = query_params.get('page', [None])[0]
        response = getpeople(f'?page={next_page}')
        data = response.json()

        all_people.extend(data['results'])

        if 'next' in data:
            next_url = data['next']
        else:
            next_url = None

    return all_people

if __name__ == "__main__":
     print(get_all_people())
    #response = getpeople('?page=3')
    #response_json =response.json();
    #print(json.dumps(response_json, indent=4))