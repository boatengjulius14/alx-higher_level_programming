#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository
"rails" by the user "rails"
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
