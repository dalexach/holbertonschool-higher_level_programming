#!/usr/bin/python3

"""
    Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
        POST request to http://0.0.0.0:5000/search_user with
        the letter as a parameter.
    """
    q = argv[1] if len(argv) > 1 else ""

    try:
        url = "http://0.0.0.0:5000/search_user"
        # url = "http://7d1493591ff0.19.hbtn-cod.io:5000/search_user"
        request = requests.post(url, data={'q': q}).json()
        if 'id' in request and 'name' in request:
            print("[{}] {}".format(request['id'], request['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
