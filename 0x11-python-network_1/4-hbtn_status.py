#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


import requests

response = requests.get("https://intranet.hbtn.io/status")
print(response)