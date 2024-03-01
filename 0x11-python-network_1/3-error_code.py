#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of
the response (decoded in utf-8)."""
import sys
import urllib


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
