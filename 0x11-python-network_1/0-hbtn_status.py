#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print("    - type: {}".format(type(res)))
        print("    - content: {}".format(res))
        print("    - utf8 content:{}".format(res.decode('utf-8')))
