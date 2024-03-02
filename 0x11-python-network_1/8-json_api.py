#!/usr/bin/python3
"""Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    data = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    res = requests.post(sys.argv[1], data=data)
    res_type = res.headers['content-type']

    if res_type == 'application/json':
        _res = res.json()
        id = _res.get('id')
        name = _res.get('name')
        if _res != {} and id and name:
            print("[{}] {}".format(id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
