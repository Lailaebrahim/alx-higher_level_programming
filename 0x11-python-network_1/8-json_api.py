#!/usr/bin/python3
"""Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    res = requests.post(sys[1], data)
    res_type = res.headers['content-type']

    if res_type == 'application/json':
        id = res.json().get('id')
        name = res.json().get('name')
        if id and name:
            print("[{}] {}".format(id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
