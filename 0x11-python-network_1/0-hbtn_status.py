#!/usr/bin/python3

"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    """
        Fetching https://intranet.hbtn.io/status
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode(encoding="utf-8")))