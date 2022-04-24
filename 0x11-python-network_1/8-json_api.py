#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request to 
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import json


if __name__ == "__main__":
    import requests
    from sys import argv
    
    q = argv[1]
    if q is None:
        q = ""
    request = requests.post('http://0.0.0.0:5000/search_user')
    request_json = request.json
    print(request)
        
    