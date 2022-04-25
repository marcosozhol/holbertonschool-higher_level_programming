#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    request = requests.post('http://0.0.0.0:5000/search_user', data={"q": q})
    request_json = request.json()
    try:
        if request_json:
            print('[{}] {}'.format(request_json['id'], request_json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
