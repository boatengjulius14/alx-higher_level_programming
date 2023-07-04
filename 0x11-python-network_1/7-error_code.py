#!/usr/bin/python3
"""sends a request to the URL and displays the body
of reponse
"""


from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
