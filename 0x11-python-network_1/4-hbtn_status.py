#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests
"""


if __name__=="__main__":
    import requests

    response = requests.get("https://intranet.hbtn.io/status")

    print('Body response:')
    print('\t - type: {}'.format(type(response.text)))
    print('\t - content: {}'.format(response.text))