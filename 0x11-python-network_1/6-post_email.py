#!/usr/bin/python3
""" Python script that takes in a URL and an email address."""
import sys
import requests


if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    val = req.text
    print(val)
