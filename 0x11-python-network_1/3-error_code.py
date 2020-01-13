#!/usr/bin/python3

"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""

import urllib.request
from urllib.error import URLError, HTTPError
import sys


if __name__ == "__main__":
    """
        Sending a request
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            r = html.decode(encoding="utf-8")
            print(r)
    except URLError as err:
        print("Error code: {}".format(err.code))
