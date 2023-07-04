#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

    _data = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    request_obj = requests.post(url, data=_data)

    try:
        response = request_obj.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
