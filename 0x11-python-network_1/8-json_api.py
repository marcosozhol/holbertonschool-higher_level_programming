#!/usr/bin/python3
"""
 script that takes in a letter and
 sends a POST request
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        resp = r.json()
        if resp:
            print("[{}] {}".format(resp["id"], resp["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")