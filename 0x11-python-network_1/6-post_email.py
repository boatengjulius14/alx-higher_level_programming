#!/usr/bin/python3
"""Takes in a URL and and email address, sends a POST
request to the passed URL with the email as a parameter
and displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":
    value = {"email": argv[2]}

    response = requests.post(argv[1], data=value)
    print(response.text)
