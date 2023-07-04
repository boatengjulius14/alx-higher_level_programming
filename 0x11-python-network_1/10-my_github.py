#!/usr/bin/python3
"""takes GitHub credentials and uses the GitHub API to
display its id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    api_endpoint = "https://api.github.com/user"
    response = requests.get(api_endpoint, auth=auth)
    user_data = response.json()
    user_id = user_data.get("id")
    print(user_id)
