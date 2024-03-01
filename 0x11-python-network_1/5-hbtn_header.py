#!/usr/bin/python3
"""a Python script that takes in a URL,
 sends a request to the URL and displays the value of
the variable X-Request-Id in the response header"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    val = req.headers.get('X-Request-Id')
    print(val)
