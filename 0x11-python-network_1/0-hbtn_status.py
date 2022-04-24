#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
  

if __name__ == "__main__":
    import urllib.request
    
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        the_page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(type(html)))
        print('\t- utf8 content: {}'.format(html.decode("utf8, replace")))