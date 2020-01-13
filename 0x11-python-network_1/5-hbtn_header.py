#!/usr/bin/python3

"""
    Python script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
    using the package requests
"""

import requests
import sys


if __name__ == "__main__":
    """
        Using the package Requests
    """
    arg = sys.argv[1]
    response = requests.get(arg)
    print(response.headers.get('X-Request-Id'))
