#!/usr/bin/python3

"""
    Python script that takes in a string and sends a search
    request to the Star Wars API
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
        Searching a request to the Star Wars API
    """
    value = {'search': argv[1] if len(argv) > 1 else ""}
    try:
        url = "https://swapi.co/api/people"
        response = requests.get(url, params=value).json()
        counter = response.get("count")
        print("Number of results: {}".format(counter))
        if counter > 0:
            for result in response.get("results"):
                print(result['name'])
    except ValueError:
        print("Not a valid JSON")
