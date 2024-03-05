#!/usr/bin/python3
"""a Python script that takes 2 arguments
Please list 10 commits (from the most recent to oldest) of the repository
 “rails” by the user “rails”"""
from sys import argv
import requests


if __name__ == "__main__":
    url = ("https://api.github.com/repos/{}/{}/commits"
           .format(argv[2], argv[1]))
    url = url + "?per_page=10"
    res = requests.get(url).json()
    for val in res:
        sha = val.get('sha')
        author = val.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
