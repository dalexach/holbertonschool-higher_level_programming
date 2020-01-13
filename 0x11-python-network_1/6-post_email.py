#!/usr/bin/python3

"""
    Python script that takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter, and finally
    displays the body of the response.
    using the package requests
"""

import requests
import sys


if __name__ == "__main__":
    """
        Using the package Requests to send POST request
    """
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    response = requests.post(url, value)
    print(response.text)
