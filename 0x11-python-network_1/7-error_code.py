#!/usr/bin/python3

"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response. Using package requests
"""

import requests
from requests.exceptions import HTTPError
import sys


if __name__ == "__main__":
    """
        Display the body response, if its error code print it
    """
    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if code > 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
