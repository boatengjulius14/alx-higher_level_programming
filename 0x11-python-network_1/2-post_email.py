#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body
of the response
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')

    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
