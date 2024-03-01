#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
 and displays the body of the response (decoded in utf-8)"""
import sys
from urllib import parse, request


if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode('ascii')
    with request.urlopen(sys.argv[1], data) as response:
        res = response.read().decode('utf-8')
        print(res)
